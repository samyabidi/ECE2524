#include <unistd.h>
#include <sys/wait.h>

#include <string>
#include <vector>
#include "Process.h"
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
//#include <sys/type.h>
#include <sys/wait.h>

Process::Process(const std::vector<std::string> &args)
{
    if( pipe(readpipe)<0)
    {
            perror("create read pipe");
         }
         
     if(pipe(writepipe)<0)
     {
            perror("create write pipe");
         }
    m_pid = ::fork();
        if(m_pid == 0)
            {
            
           // close(STDIN_FILENO);
           //  close(STDOUT_FILENO);
          // dup2(writepipe[1],1);
          
         std::cerr<<("in child \n");
        if(  dup2(writepipe[0],STDIN_FILENO)<0)
        {
            perror("dup2 write pipe");
        }
         if( dup2(readpipe[1],STDOUT_FILENO)<0)
         {
            perror("dup2 read pipe");
         }
         if( close(writepipe[0])<0)
         {
            perror("close write 0");
         }
          if(close(readpipe[1])<0)
          {
            perror("close read 1");
         }
         if( close(writepipe[1])<0)
         {
            perror("close write 1");
         }
          if(close(readpipe[0])<0)
          {
            perror("close read 0");
         }
          std::cerr<<("calling execve \n");
            ::execve("./consumer", NULL, NULL);
            exit(0);
            }
            close(writepipe[0]);
          close(readpipe[1]);
   
             
             
          
}

void Process::write(const std::string& temp)
{
    
    //close(writepipe[0]);
    //std::cerr<<("PROCESS::WRITE \n");
    ::write(writepipe[1],temp.c_str() , temp.size()); 
}

std::string Process::readline()
{
    //close(readpipe[1]);
   // std::cerr<<("PROCESS::READ \n");
    
    int size = ::read(readpipe[0] ,value, sizeof(value));
    value[size] = 0;
    return value;
}

Process::~Process()
{
     close(writepipe[1]);
          close(readpipe[0]);

}
