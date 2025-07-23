import csv
import uuid
import requests
import os

GITHUB_TOKEN='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'
headers={'Authorization': f'token {GITHUB_TOKEN}'}

keywords=['quant','pnl','alpha','risk','strategy','backtesting']
lang=['Python','C++']

def search_repo():
    query='quant+language:Python+stars:>1'
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page=11"
    response=requests.get(url,headers=headers)
    return response.json().get('items',[])

def analyze_filter(repos):
    devs={}
    for repo in repos:
        owner=repo['owner']['login']
        link=repo['owner']['html_url']
        language=repo.get('language','')
        star=repo['stargazers_count']
        if language not in lang or star<1:
            continue
        if owner not in devs:
            devs[owner]={
                'name':owner,
                'github_link':link,
                'star_total':0,
                'repo_count':0
                }
        devs[owner]['repo_count']+=1
        devs[owner]['star_total']+=star

    qualified_devs=[]
    for dev in devs.values():
        if dev['repo_count'] >=2 or dev['star_total']>=10:
            dev['score']=dev['star_total']+dev['repo_count'] *5
            qualified_devs.append(dev)
    return qualified_devs

def save_csv(developers):
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    output_path = os.path.join(script_dir, "developers.csv")

    with open(output_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "github_link", "repo_count", "star_total", "score"])
        writer.writeheader()
        for dev in developers:
            writer.writerow(dev)


def integrity_token():
    return str(uuid.uuid4())

if __name__ == "__main__":
    print('Integrity Token:',integrity_token())
    repos=search_repo()
    filtered_dev=analyze_filter(repos)
    save_csv(filtered_dev)
    print('Done: Output saved to csv file')


        

            
