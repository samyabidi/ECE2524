#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
//#include <sys/type.h>
#include <sys/wait.h>






int main()
{
    int ab[2];
    pipe(ab);
    int status;
    int proc1, proc2;
    pid_t pid[2];
int n;

pid[0]=fork();
if(pid[0] == 0)
{       dup2(ab[1], STDOUT_FILENO);//connect output to write end of pipe
        close(ab[0]);//closing read end of pipe
        execve("./generator", NULL, NULL);
        exit(0);
}

pid[1]=fork();
if(pid[1] == 0)
{       dup2(ab[0], STDIN_FILENO);//connecting input to read end
        close(ab[1]);//closig write end of pipe
        execve("./consumer", NULL, NULL);
        exit(0);
}

sleep(1);

kill(pid[0],SIGTERM);
proc1 = waitpid(pid[0], &status, 0);
std::cerr<<"child["<<proc1<<"] exited with status "<<status<<std::endl;

//close all portals
 close(ab[0]);
 close(ab[1]);
proc2 = waitpid(pid[1], &status, 0);
std::cerr<<"child["<<proc2<<"] exited with status "<<status<<std::endl;
// Only the parent will be running outside of those if statements.
// Essential: close all other pipes and copies of pipes


    
    return 0;
}






















