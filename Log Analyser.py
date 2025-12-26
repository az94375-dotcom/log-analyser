import re

def parse_failed_logins(filepath):
    failed_count=0
    user_failure={}
    ip_failure={}
    
     
     
    with open(filepath, "r") as file:
    
        for line in file:
            lowercase=line.lower()
            
            if "failed password" in lowercase:
                failed_count +=1
                parts=lowercase.split()
                
                
                username = None
                ip=None
            # Case 1: "invalid user <username>"
                if "invalid" in parts and "user" in parts:
                    user_index = parts.index("user")
                    username = parts[user_index + 1]

            # Case 2: "for <username>"
                elif "for" in parts:
                    for_index = parts.index("for")
                    username = parts[for_index + 1]

                #if username:
                #print("Extracted Username:", username)
            
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
                if ip:
                    if ip not in ip_failure:
                        ip_failure[ip]=1
                    else:
                        ip_failure[ip]+=1

    return failed_count, user_failure,ip_failure

failed_count, user_failure,ip_failure=parse_failed_logins("sample_logs.txt")
                
def build_report(failed_count, user_failure, ip_failure):
    lines = []

    lines.append("==== FAILED LOGIN SUMMARY ====")
    lines.append(f"Total Failed login attempts: {failed_count}")
    lines.append("")

    lines.append("Failed Usernames:")
    for username, count in user_failure.items():
        lines.append(f"{username} : {count}")

    lines.append("")

    lines.append("Failed IPs:")
    for ip, count in ip_failure.items():
        lines.append(f"{ip} : {count}")

    report_text = "\n".join(lines)
    return report_text

report = build_report(failed_count, user_failure, ip_failure)
print(report)
