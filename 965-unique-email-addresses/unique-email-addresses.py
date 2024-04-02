class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        emailSet = set()

        for email in emails:
            emailList = email.split("@")
            e = []
            for char in emailList[0]:
                if char == "+":
                    break
                if char != ".":
                    e.append(char)
                
            e.append("@")
            e.append(emailList[1])
            emailSet.add("".join(e))
        
        return len(emailSet)

        