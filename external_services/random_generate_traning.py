from datetime import datetime

from lexicon import day_task as task


def generate_training() -> str:
    now = datetime.now()
    weekday = datetime.weekday(now)
    print(weekday)
    match weekday:
        case 0:
            return task.MONDAY
        case 1:
            return task.TUESDAY
        case 2:
            return task.WEDNESDAY
        case 3:
            return task.THURSDAY
        case 4:
            return task.FRIDAY
        case 5:
            return task.SATURDAY
        case 6:
            return task.SUNDAY


if __name__ == "__main__":
    print(generate_training())