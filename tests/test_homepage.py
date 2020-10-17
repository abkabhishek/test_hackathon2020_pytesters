
import time
"""

"""
# def test_title(app):
#     app.home_page.open_home_page()
#     assert (app.home_page.get_title() == "Coronavirus Outbreak in India - covid19india.org")


def test_top_3_status_confirmed_count(app):
    app.home_page.open_home_page()
    time.sleep(3)
    app.home_page.click_deceased_sort_desc()
    time.sleep(3)
    x = app.home_page.get_nth_state_name(1)
    print(x)
    # assert ( x== "Odisha")
    x = app.home_page.get_nth_state_confirmed_count(1)
    print(x)
    # assert (x == 266345)
    x =app.home_page.get_nth_state_active_count(1)
    print(x)
    # assert (x == 23786)
    x =app.home_page.get_nth_state_recovered_count(1)
    print(x)
    # assert ( x== 241385)
    x = app.home_page.get_nth_state_deceased_count(1)
    print(x)
    # assert ( x== 1174)
    x = app.home_page.get_nth_state_tested_count(1)
    print(x)
    # assert ( int(x)== 4001065)