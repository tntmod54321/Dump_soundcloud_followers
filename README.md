#### A lil' script to dump a user's soundcloud followers  
> This is my first python script  
> (I've only used ahk/batch/applescript/shell/html/js before, so not really any kind of file reading/writing stuff)  
> so if it's bad code don't shoot me, it does the job and I even made it so I'm not constantly opening and closing the file, that's gotta > count for something, right? : )  
  
You need 2 things to run this script,  
1. A soundcloud API key, you can try to get one legitimately but good luck with that man, they haven't been accepting API key requests in years.  
If you want to get one you can just go ctrl+i -> network -> sort by xhr and find any request where the url has &client_id= in it and swipe that id, it's an API key you can use (and it's unique to your account so don't share it).  
2. The *NUMERICAL id* of the user you want to dump the followers from.  
