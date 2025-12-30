from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.schemas import ProcessedUser
from app.services.fetch import fetch_logtime, fetch_evals_as_corrector, fetch_evals_as_corrected
from app.services.projects import get_project
import json

def is_processed_fresh(processed, update_frame) -> bool:
    if not processed or not processed.updated_at:
        return False

    return processed.updated_at > (
        datetime.now(timezone.utc)
        - timedelta(seconds=update_frame)
    )


def format_data(user: ProcessedUser) -> list[dict]:
    # return user
    ret = {
        "id": user.id,
        "intra": user.ft_user.login,
        "evaluated_total_evals": user.evaluated_total_evals,
        "evaluated_avg_grade": user.evaluated_avg_grade,
        "evaluated_avg_time": user.evaluated_avg_time,
        "evaluated_top": user.evaluated_top,
    }
    return ret


def insert_processed_user(user: ProcessedUser, db: Session):
    pass


def trim_evals_data(data: list[dict]) -> list[dict]:
    return data
    #keep
    # intra,
    # start time,
    # end time,
    # grade


class Evaluator:
    def __init__(self, login):
        self.login = login
        self.count = 0
        self.tot_mark = 0

    def addEval(self, mark):
        self.count += 1
        self.tot_mark += mark


def parse_corrected_data(evals: list[dict], db: Session) -> list[dict]:
    """Returns JSON"""
    total = 0
    tot_grade = 0
    tot_time = 0
    invalid = 0
    evaluators = {}

    for eval in evals:
        p = get_project(eval['team']['project_id'], db)
        if p.cursus == "C Piscine":
            continue

        if eval['truant']:
            invalid += eval['truant']['login'] == eval['correcteds'][0]['login']
            continue

        if not eval['corrector']['login'] in evaluators:
            evaluators[eval['corrector']['login']] = { 'tot_mark': eval['final_mark'], 'count': 1}
        else:
            evaluators[eval['corrector']['login']]['tot_mark'] += eval['final_mark']
            evaluators[eval['corrector']['login']]['count'] += 1

        begin = datetime.fromisoformat(eval["begin_at"].replace("Z", "+00:00"))
        filled = datetime.fromisoformat(eval["filled_at"].replace("Z", "+00:00"))
        total += 1
        tot_grade += eval['final_mark']
        tot_time += (filled - begin).total_seconds()

    res = sorted(evaluators.items(), key=lambda x: x[1]['count'], reverse=True)
    res = [{"login": login, **stats} for login, stats in res]
    return {
        "total": total,
        "avg_grade": tot_grade / total if total != 0 else 0,
        "avg_time": tot_time / total if total != 0 else 0,
        "top": res[:3],
        "invalid": invalid
    }


def parse_corrector_data(evals: list[dict], db: Session) -> list[dict]:
    pass


def build_processed_from_raw(id: int, db: Session):
    """Retrieves the processed user linked to id, builds the processed fields if necessary, and commits it"""
    raw_processed = db.query(ProcessedUser).filter(ProcessedUser.id == id).first()

    #dont build if fields are already there tho

    print("raw_processed: ", raw_processed.__dict__)
    corrected_data = parse_corrected_data(raw_processed.raw_evals_corrected, db)
    # if corrected_data is None:
    #     raise RuntimeError(corrected_data)
    raw_processed.evaluated_total_evals = corrected_data['total']
    raw_processed.evaluated_avg_time = corrected_data['avg_time']
    raw_processed.evaluated_avg_grade = corrected_data['avg_grade']
    raw_processed.evaluated_top = corrected_data['top']

    # corrector_data = parse_corrector_data(raw_processed.raw_evals_corrector, db)
    # raw_processed.evaluator_total_evals = corrector_data['total']
    # raw_processed.evaluator_avg_time = corrector_data['avg_time']
    # raw_processed.evaluator_avg_grade = corrector_data['avg_grade']


    db.add(raw_processed)
    db.commit()
    db.refresh(raw_processed)
    # corrector_data = get_evals_data(raw_processed.raw_evals_corrector)


def fetch_and_insert_raw_processed_user(id: int, db: Session):
    """calls 42API, and builds a raw processed user without computation"""
    # logtime = fetch_logtime(id)
    # as_corrector = fetch_evals_as_corrector(id)
    as_corrected = fetch_evals_as_corrected(id)
    processed = ProcessedUser(
        id=id,
        raw_logtime=None,
        raw_evals_corrector=None,
        raw_evals_corrected=as_corrected,
        # raw_logtime=logtime,
        # raw_evals_corrector=as_corrector,
    )
    db.add(processed)
    db.commit()
    db.refresh(processed)
