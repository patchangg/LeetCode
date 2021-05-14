
def numUniqueEmails(emails):
    dict = {}
    for email in emails:
        local,domain = email.split("@")
        local = local.replace('.','')
        if "+" in local:
            local = local.split("+",1)[0]
        combine = local + "@" + domain
        if combine not in dict:
            dict[combine] = 1
    output = list(dict.keys())
    return len(output)



emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
numUnique = numUniqueEmails(emails)
print(numUnique)
