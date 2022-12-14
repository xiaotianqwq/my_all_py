from revChatGPT.revChatGPT import Chatbot

# For the config please go here:
# https://github.com/acheong08/ChatGPT/wiki/Setup
config = {
    "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..fIJks59VVwdVhxr2.NLFvskyEg8Rp8Y2enFu2Z-A99nTTt0TVsigKzKT9QL4t3G1SUygx0I9ZhXnv77N08w8LjUrQBTCso9cFkSgc1x7df1FuWkHqEscWBBzN7OISLSJ8lJ32ZkT7BmaqnYdcnKhDKAlVq7pdMguX9ILkQbfQWfoTfHQ8a1LVug7d3W0EfKhU6yIgmdfb4oTLAYOi7jFQcL_hZs-gKHr7fj1BM7QA1lQ2PJleHL3mZ7lQNdwV_lYEUiyxweh4ZiyXqbGywKKNfnAxSJushB3hJLgXY8r8b3xC7lWoL_FSLjqTGdGwDP2TD_Au7R_BnumkQHEP4br0wN31x-LpZ1NiBkmKq3DC2cVSrxtc1amaFC1dUrz7lDwE_CPX_U7VG3ZO6ZzXI3phwYwWc-cHdwWwy359E22dkw6XBQ1j3zKDZOlQYs0KQ41Ix9EyD-i9JMu8xCLakODC7K7Taokt8ce-KznS6XRShVn9uf8mVFD67Fcvqwd13OqXofOL3S_3KWje8raTh8WEP38-zuFVGVBhpHUxydwiibLKgMVTYu5u2VNQWnh16Inb9-bzJaZMijw3ZUZmTUk_7vIhCvge14_Vp7083aBBcMB86pHbTB8qqRhdfo10LEx9tPh8JRgEtHDZPDJK1crEDOl-WSs079-LsjNczxcTlB5pfdc2iC8PZt452kE5cc8gv3Z7F0tKJd4ICrBE0h8x-8zY-6WEkhoQUmcjNL42gXnZsTA-8DFvQ0YypV_vWZ1II31B4Pu_axnqiwUj8jkxcty_VsTlh0h39FL0s-dW15moFFaHGCSEGGKrQtCWdZOWky4ATaOc_ldd4el9f91cdWpu2oH1qgErOu9JFmsM_8zPLazesUHRRHn5ty-zSLduJMBnc5qVmXHTqTuSEg_y9NhliC5nyUTCW0Wne_mh3ryWPgvP6hWzj66-pFwhzgwmeLllpQSvZPvg80kpnWNabBOgn4LoW8gsw2iJcGm2jHWwX73glTMqdCIYqCLrkQaMKLqnMlIJMllhwiDQvkq__FdMzP5-psaqZ7llrPniO6oa48aLuU_wVTXEPyQCO5l0UgdbOcQmXXu2zD_LLgxZWKt9Epw2QDwidRPGkA4CYPW9mRj7ZyVwiGVqHg7E_GzWNVjNozCq774lPJiNwAu-Z37sZhFVPCxC4HzP-Hf5knDedBHq_CIRTXqh69-x8d_q1W-4lpNAbkCCzNlqd_IoGaeeaFa4RZveShEOAxzNEcB1CsYhcmSl9lEARKxG0wMILefEUKSKyeTzLv_znqHdE2aV7WB_E5S2x7c-JLr5ISecKtzZWKzr310jfPyOvPZ9SlKU2naW32AoLt8s6Q3Wj9hP8NFr_5T1YhR0yTwp6QFYuLYvg3NLFoa3afXaBCqhEB3y0eq_lfS7ZDClkHYYJMeOC1upcG-JMf1R-y7ymRkwEkqtO6KM7o8cuaCbRfMDPNGEO3oq00d1qpokdsTWGxRNEiM41k8VWjmQtNUGzWSy2vyryvr1Oc3CqG-Sz242fC8j0-y85002oJSsMJFUOnj1RVgFXNzdG7oFrZOwze3mk4e-V1f1IpXbw0D3N_aIlcT28GJK0MjhH9QIOCvcYhzPnh53yYH2cUTdy0lXEipqO0ednAcFk4FrLGCDspf7iytxKXiNaMOsOmNHm7BqOCuskeYlHecQQX2ubGsishPfUR_YlMDjW1s4HPidmxeZxy6xpp_NIZkKcwWeYY3zCy_k0XBRtuaiyGYOV-xiBMnccw7Tt3O1STLl34jc3DUJAVw6P6W_7cLU4A7C1Zdc92amFxtMq9BgOPN_GYicxaFPvskCMbG4wujU44E85fFjRxl6u0YF2OChX3yEfRzOI-up0ADkBLQmlvDLisSVyX-GTcuMGsRBYpYtDuMQLhpi4pf7H0Cmq0jdN8i_U5RFW0JeGMhCysZ5Y3IS_EAcKl0DNEhoZO65JB03Z4nuZlk76ysIBAleJaiGx2EnxygoJQ-LwuXWdNVGW7_aLb925n8Wz1YkQXtQQyZDB4YE20hbXhYR_lWAemC-2-eymfFTMdokiy6aDrgTLBu1WPOvfTUC4ZT3Otpw2uf9AHZx-S_htIQ1w0nutOPdGLcmzAQLI_3TPNwJl6jpVzFUZONFRzm8Cs-7sboU72_GZ7AnGH6t_BDc0GJjriJtoTAIx47gRS6zEjXizsbCdrqTWpHgfzrlWCdF8wC7Nt320KTIahib9AFl4Agy75TyFXmlA7sKtgmO608TRZPN.MjyYeltAwxl2c13Gzb_Tiw",
}

chatbot = Chatbot(config, conversation_id=None)


def __init__(self, config, conversation_id=None, debug=False, refresh=True):
    """
    :param config: Config dict
    :param conversation_id: Conversation ID. If None, a new conversation will be created
    :param debug: Debug mode, Default is False
    :param refresh: Refresh the session token, Default is True
    """

#
# def reset_chat(self): ->
#
#
# None
#
#
# def refresh_headers(self): ->
#
#
# None


def generate_uuid(self):  # Internal use
    def get_chat_stream(self, data):  # Internal

        def get_chat_text(self, data):  # Internal

            def get_chat_response(self, prompt, output="text"):
                """
        :param prompt: The message sent to the chatbot
        :param output: Output type. Can be "text" or "stream"
        :return: Response from the chatbot
        """


def rollback_conversation(self):
    """
    Rollback the conversation to the previous state
    :return: None
    """


def refresh_session(self):
    """
    Refresh the session token
    :return: None
    """


def login(self, email, password):
    """
    :param email: Email
    :param password: Password
    """

... # After the initial setup
# The text output

response = chatbot.get_chat_response("Hello world", output="text")
print(response)

# returns {'message':message, 'conversation_id':self.conversation_id, 'parent_id':self.parent_id}