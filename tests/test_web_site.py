from pages.web_site_pages import WebsitePage


def test_contact_details(browser_open):
    website=WebsitePage(browser_open)
    website.click_contact_button()
    website.set_up_managed_services()
    website.click_continue_button()
    website.choose_application_engeenering()
    website.click_continue_button()
    website.choose_team_members()
    website.click_continue_button()
    website.start_event()
    website.click_continue_button()
    assert website.find_elements()==['Name', 'Work email', 'Company','Anything else']




