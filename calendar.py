import argparse
import calendar
from datetime import date


def main() -> None:
    today = date.today()
    parser = argparse.ArgumentParser(description="Display a monthly calendar.")
    parser.add_argument(
        "--month",
        type=int,
        choices=range(1, 13),
        default=today.month,
        help="month to display (1-12; defaults to the current month)",
    )
    parser.add_argument(
        "--year",
        type=int,
        default=today.year,
        help="year to display (defaults to the current year)",
    )
    args = parser.parse_args()

    month_calendar = calendar.TextCalendar(firstweekday=calendar.SUNDAY)
    print(month_calendar.formatmonth(args.year, args.month), end="")


if __name__ == "__main__":
    main()