import time
"""

"""
#
# def test_title(app):
#     app.home_page.open_home_page()
#     assert (app.home_page.get_title() == "Coronavirus Outbreak in India - covid19india.org")
#
#
#
# def test_top_3_status_confirmed_count(app):
#
#     # call the api to get top 3 state data:
#     top_3_states = app.api.fetch_get_details(3)
#     print(top_3_states)
#     app.home_page.open_home_page()
#     #Iterating over all status.
#     for k,v in top_3_states.items():
#         row_count = app.home_page.get_row_count_by_state_name(k)
#         state_confirmed_count = app.home_page.get_nth_state_confirmed_count(row_count)
#         state_active_count = app.home_page.get_nth_state_active_count(row_count)
#         state_recovered_count = app.home_page.get_nth_state_recovered_count(row_count)
#         print(k,state_confirmed_count,state_active_count,state_recovered_count)
#         print("Validating values for State " +k )
#         print("Validating confirmed cases - Actual: {}, expected :{} ".format(v["confirmed"],state_confirmed_count))
#         assert (v["confirmed"] == state_confirmed_count)
#         print("Validating active cases - Actual: {}, expected :{} ".format(v["active"],state_active_count))
#         assert (v["active"] == state_active_count)
#         print("Validating recovered cases - Actual: {}, expected :{} ".format(v["recovered"],state_recovered_count))
#         assert (v["recovered"] == state_recovered_count)

def test_top_3_status_district_wise_data(app):

    # call the api to get top 3 state data:
    top_3_states = app.api.fetch_get_details(3)

    app.home_page.open_home_page()
    # Iterating over all status
    for k,v in top_3_states.items():
        time.sleep(3)
        state_data = app.api.get_district_data(top_3_states[k])
        print(state_data)
        row_count = app.home_page.get_row_count_by_state_name(k)
        if(app.home_page.click_nth_state_page_link(row_count)):
            print(app.state_page.get_all_districts_data())


