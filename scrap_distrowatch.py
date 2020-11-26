from os import path
import requests
from requests_html import HTML, Element
import pandas as pd
import pickle

mlen = 50

18002587170
7864-826615





class DistroWatchURLS:
    current_url = None
    _base_url = "https://distrowatch.com/index.php?dataspan="
    Year_2002_url = _base_url + "2002"
    Year_2003_url = _base_url + "2003"
    Year_2004_url = _base_url + "2004"
    Year_2005_url = _base_url + "2005"
    Year_2006_url = _base_url + "2006"
    Year_2007_url = _base_url + "2007"
    Year_2008_url = _base_url + "2008"
    Year_2009_url = _base_url + "2009"
    Year_2010_url = _base_url + "2010"
    Year_2011_url = _base_url + "2011"
    Year_2012_url = _base_url + "2012"
    Year_2013_url = _base_url + "2013"
    Year_2014_url = _base_url + "2014"
    Year_2015_url = _base_url + "2015"
    Year_2016_url = _base_url + "2016"
    Year_2017_url = _base_url + "2017"
    Year_2018_url = _base_url + "2018"
    Year_2019_url = _base_url + "2019"
    Last_12_months_url = _base_url + "52"
    Last_6_months_url = _base_url + "26"
    Last_3_months_url = _base_url + "13"
    Last_30_days_url = _base_url + "4"
    Last_7_days_url = _base_url + "1"
    Average_Rating_url = _base_url + "score"
    Most_Ratings_url = _base_url + "votes"
    Trending_past_12_months_url = _base_url + "trending-52"
    Trending_past_6_months_url = _base_url + "trending-26"
    Trending_past_3_months_url = _base_url + "trending-13"
    Trending_past_30_days_url = _base_url + "trending-4"
    Trending_past_7_days_url = _base_url + "trending-1"

class DistroWatch(DistroWatchURLS):
    def url_to_text(self, filename=None, directory=None, save=False, verbose=False):
        assert isinstance(self.url, str), f"[-] {self.url} not string"
        if save:
            verbose and print("[*] save=True")
            assert isinstance(filename, str), f"[-] '{filename}' not string"
            if directory:
                verbose and print(f"[*] directory={directory}")
                assert path.exists(directory), f"'{directory}' doesn't exists"
                assert filename[0] != "/", f"directory={directory} and filename={filename}, both cannot be defined simultaneously"
                filename = path.join(path.abspath(directory), filename)
                verbose and print(f"[*] filename={filename}")
            assert not path.exists(filename), f"{filename} already exists"

        with requests.get(url=self.url) as response:
            verbose and print(f"response={response}")
            rtext = response.text
            if save:
                with open(file=filename, mode="w") as file_obj:
                    file_obj.write(rtext)
                    verbose and print(
                        f"[*] {rtext[:mlen]}... written in {filename}")
                    return True
            else:
                verbose and print(
                    verbose and f"[*] rtext='{rtext[:mlen]}...'")
                return rtext
        return False
    
    def set_url(self, url):
        assert url in DistroWatchURLS.__dict__.value(), "[-] Invalid url: Pass DistroWatchURLS.[someurl from autocomplete]"
        self.current_url = url


if __name__ == "__min__":
    url = "https://distrowatch.com/index.php?dataspan=trending-1"
    html_text = url_to_text(url=url, verbose=False)
    html_obj = HTML(html=html_text)
    dataspans = html_obj.find(selector="select[name='dataspan']")
    selected_option = dataspans[0].find("option[selected]")[0]
    print(selected_option)
    print(selected_option.attrs['value'])
    for dataspan in dataspans:
        print(dataspan)
    headers = html_obj.find("th.News")
    columns = []
    for first_index in range(len(headers)-3):
        if headers[first_index].text.strip() == "Rank" and headers[first_index+1].text.strip() == "Distribution":
            columns = [
                headers[first_index].text.strip(),
                headers[first_index+1].text.strip(),
                headers[first_index+2].text.strip()
            ]
            break

    ranks = html_obj.find(".phr1")
    distros = html_obj.find(".phr2")
    trend_shifts = html_obj.find(".phr3")
    trends_table = []
    for rank, distro, trend_shift in zip(ranks, distros, trend_shifts):
        trends_table.append([rank.text, distro.text, trend_shift.text])
    df = pd.DataFrame(trends_table, columns=columns)
    df.to_csv(filename+".csv", index=False)

if __name__ == "__main__":
    p = DistroWatchURLS.__dict__.values()
    print(p)
