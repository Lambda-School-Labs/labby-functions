# Core imports
import os
from functools import lru_cache

# Third party imports
from airtable import Airtable

SMT_BASE_ID = "appvMqcwCQosrsHhM"

STUDENTS_SURVEYS_TABLE = "Labs - TBSurveys"


def get_all_student_surveys(cohort: str) -> list:
    """
    Retrieves records for all students onboarding surveys in a cohort

    Note: Surveys are gathered from a view on the survey table with the same
          name as the `cohort` parameter.

    Returns:
        records (``list``): List of student survey records
    """
    students_table = Airtable(SMT_BASE_ID, STUDENTS_SURVEYS_TABLE, api_key=os.environ["AIRTABLE_API_KEY"])

    return students_table.get_all(view=cohort)


@lru_cache
def get_student(record_id: str) -> list:
    """
    Retrieves the student record ID

    Returns:
        record: The student record
    """
    students_table = Airtable(SMT_BASE_ID, STUDENTS_SURVEYS_TABLE, api_key=os.environ["AIRTABLE_API_KEY"])

    return students_table.get(record_id)
