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

    match args.command:
        case 'add':
            create_task(args.title)
        case 'list':
            list_tasks()
        case 'done':
            complete_task(args.id)
        case 'delete':
            remove_task(args.id)
        case _:
            print("Noto'g'ri command")

if __name__ == "__main__":
    main()
