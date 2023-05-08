import os
import sys


def main():
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ehs.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Can't import Django. Are you sure it is installed "
            
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
