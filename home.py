

import streamlit as st
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown("<p style='text-align:right;'><strong>cadence.music</strong></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:right;'><u><a href='home' target='_self'>home</a></u> | <a href='submit' target='_self'>submit</a> | <a href='archive' target='_self'>archive</a></p>", unsafe_allow_html=True)

st.subheader("cadence music")

st.markdown("everyone moves to their own music cadence. this community allows you to share your with others.")

st.markdown("every week, we invite our community to share a song with a brief blurb. from country to soul to UK grime, cadence submissions know no bounds. all submissions are *anonymous* to center the experience on the music rather than the person.")

st.markdown("to sign-up, simply add your email address below. see you on the other side.")

with st.form("test"):
    email = st.text_input("your email address, please")
    st.caption("we'll never share it, don't worry.")

    submitted = st.form_submit_button("subscribe")
    if submitted:
        try:
            client = MailchimpMarketing.Client()
            client.set_config({
                "api_key": "23708f224b50afb6feec9def52d73b48-us16"  
            })

            response = client.lists.add_list_member("9bb6260830", {"email_address": email, "status": "subscribed"})  
            st.success("you've subscribed")
        
        except Exception as e:
            st.error(f"an error occurred: {e}")

