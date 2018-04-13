from muse import melon, genie, bugs
import json

if __name__ == '__main__':
    print("-\n melon top 100 \n-")
    print(json.dumps(melon.get_real_time_chart_songs(), ensure_ascii=False, indent=2))

    print("-\n genie top 100 \n-")
    print(json.dumps(genie.get_real_time_chart_songs(), ensure_ascii=False, indent=2))

    print("-\n bugs top 100 \n-")
    print(json.dumps(bugs.get_real_time_chart_songs(), ensure_ascii=False, indent=2))
