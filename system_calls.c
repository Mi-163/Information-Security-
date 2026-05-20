//this program demonstrates the use of various system calls in C, including fork(), stat(), opendir(), readdir(), and execlp().
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <dirent.h>

int main()
{
    if (fork() == 0)
    {
        printf("child id: %d", getpid())

            struct stat st;

        stat("sample.txt", &st);

        printf("file size: %ld", st.st_size);

        DIR *d = opendir(".");

        struct dirent *dir;

        while ((dir = readdir()) != NULL)
        {
            printf("found %s", dir->d_name);
        }
        closedir(d);

        execlp("date", "date", NULL)

            exit(1);
    }

    else
    {
        printf("parent id: %d", getpid());

        wait(NULL);

        exit(0);
    }
}
