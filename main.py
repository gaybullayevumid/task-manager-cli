from cli.parser import create_parser
from db.database import init_db
from services.task_service import (
    create_task,
    list_tasks,
    complete_task,
    remove_task
)


def main():
    init_db()

    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        create_task(args.title)

    elif args.command == "list":
        list_tasks()

    elif args.command == "done":
        complete_task(args.id)

    elif args.command == "delete":
        remove_task(args.id)

    else:
        print("Noto‘g‘ri command")


if __name__ == "__main__":
    main()