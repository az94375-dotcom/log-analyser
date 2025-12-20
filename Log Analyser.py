import re
with open("sample_logs.txt", "r") as file:
    failed_count=0
    user_failure={}
    ip_failure={}
    for line in file:
        lowercase=line.lower()
        
        if "failed password" in lowercase:
            failed_count +=1
            parts=lowercase.split()
            
            
            username = None
            # Case 1: "invalid user <username>"
            if "invalid" in parts and "user" in parts:
                user_index = parts.index("user")
                username = parts[user_index + 1]

            # Case 2: "for <username>"
            elif "for" in parts:
                for_index = parts.index("for")
                username = parts[for_index + 1]

            #if username:
             #   print("Extracted Username:", username)
            
            #Extracting IP
            ip= re.search(r"\d+\.\d+\.\d+\.\d+", lowercase)
            if ip:
                ip=ip.group()
                #print("Extracted IP:", ip)
                
            #failures per username
            if username:
                if username not in user_failure:
                    user_failure[username]=1
                else:
                    user_failure[username]+=1
                
            #failures per ip
            if ip not in ip_failure:
                ip_failure[ip]=1
            else:
                ip_failure[ip]+=1
                
print("==== FAILED LOGIN SUMMARY ====")
print("Total Failed login attempts:", failed_count)
print("Failed Usernames\n")
for username, count in user_failure.items():
    print(username, ":" ,count)
print("Failed IPs\n")
for ip , count in ip_failure.items():
    print(ip,":", count)
    

