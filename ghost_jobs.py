from datetime import datetime,timedelta #import these for the date posted of the listing
sus_companies = [ # a list of companies that reportedly post ghost listings
    "PetSmart",
    "McDonald's",
    "Walmart",
    "CVS Health",
    "Target",
    "Kroger",
    "Dollar Tree",
    "7-Eleven",
    "Papa John's",
    "Subway",
    "IHOP",
    "Dunkin' Donuts",
    "Pizza Hut",
    "Buffalo Wild Wings",
    "Staples",
    "AutoZone"
]

sus_titles = [ # potential suspicious job titles
    "Cashier",
    "Sales Associate",
    "Customer Service Representative",
    "Store Clerk",
    "Shift Leader",
    "Team Member",
    "Stocker",
    "Barista",
    "Server",
    "Cook",
    "Line Cook",
    "Delivery Driver",
    "Pizza Maker",
    "Kitchen Staff",
    "Front Desk Associate",
    "Warehouse Associate",
    "Retail Associate",
    "Assistant Manager",
    "Shift Supervisor",
    "Host/Hostess"
]


def get_job_data(): # this function gets the data from the csv with the job listing in it
    data_list=[]
    
    with open("jobs.csv","r") as file:
        lines=file.readlines()
        if len(lines)>1:
            second_row=lines[1].strip()
            data_list=second_row.split(",")

        job_title=data_list[0]  # assigns the data from the csv to variables in the correct type
        company_name=data_list[1]
        num_applicants=int(data_list[3])
        date_posted=data_list[2]
        is_reposted=data_list[4].lower()=="true"
        desc=data_list[5]
        
        return job_title,company_name,date_posted,num_applicants,is_reposted,desc

def red_flags(title,company,date,num_applicants,is_reposted,desc): #takes the variables from the csv as inputs for checks
    score=0 # ghost job score
    list_desc=list(desc)
    posted_date = datetime.strptime(date, "%Y-%m-%d").date() # converts the date from the file to a python friendly format
    
    # Get today's date
    today = datetime.today().date()
    
    # Calculate the difference
    delta = today - posted_date

    if is_reposted==True:
        score+=1
    
    if len(list_desc) <50: 
        score+=2
    
    if num_applicants<5 and delta>= timedelta(days=60):
        score+=3
    
    if company in sus_companies and title in sus_titles:
        score+=1 
    elif title=="":
        score+=1
    return score

def is_ghost(score):
    if score >=0 and score <=2:
         print("Legitimate posting")
    elif score >=3 and score<=5:
         print("Likely Ghost: Some red flags")
    elif score >=6: 
        print("High Chance	Multiple red flags — very suspicious")
    

def main():
    job_title,company_name,date_posted,num_applicants,is_reposted,desc=get_job_data()
    
    is_ghost(red_flags(job_title,company_name,date_posted,num_applicants,is_reposted,desc))
if __name__=="__main__":
    main()