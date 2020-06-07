FYI if you're dumping more than one user's follower list you should prolly just fork it and make it more convenient (passing args via command line, timestamped filenames, etc...) I just really can't be assed.  
#### A lil' script to dump a user's soundcloud followers  
> This is my first python script  
> (I've only used ahk/batch/applescript/shell/html/js before, so not really any kind of file reading/writing stuff)  
> so if it's bad code don't shoot me, it does the job and I even made it so I'm not constantly opening and closing the file, that's gotta > count for something, right? : )  
  
You need 2 things to run this script,  
1. A soundcloud API key, you can try to get one legitimately but good luck with that man, they haven't been accepting API key requests in years.  
If you want to get one you can just go ctrl+i -> network -> sort by xhr, reload the page and find any request where the url has &client_id= in it and swipe that id, it's an API key you can use (and it's unique to your account so don't share it).  
2. The *NUMERICAL id* of the user you want to dump the followers from.  
this isn't their custom url (e.g. soundcloud.com/zalinki), or if their name is of the format (soundcloud.com/user-69696969) then that number isn't their id either.  
You have to go to their followers page and do the previous ctrl+i method to find a url along the format of followers?client_id= and go to that page, in the url it should be like "soundcloud.com/users/694201337/other_garbage" and the number after /users/ is their numerical id.  
  
Then plop those 2 strings into the script and run it and it'll generate a file called "follower_list_(their numerical id).txt"  
Keep in mind if you run the script on the same user again it'll just append the start of the next dump to the end of the last one, I don't feel like adding in the ability to not have duplicate users
