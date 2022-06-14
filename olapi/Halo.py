#import config
from flask import jsonify
import json
import requests


class halo_tickets:

    def __init__(self):
        self.bearer = 'CfDJ8CqpnwNtj71Ispi12IQp1FDoJPGESi4YorVbM6ZivI9MawOFEoMOWRyfatnsrx7HgWi9SAU5d6oXjf5XmU6YUqR_6mkV078mynC1OOfkh55n4QQie1_sp8NFyBvJZEsRs8OvfYN4yyY9CND5BtLCkQskBJkZWKIaDWMO8Xbt_5XoOn1zrAqV6o2aL8QCgX2eGLtrKCeH95-esacL3eVlJrdI5mYF1EjRbaCTscsqVhpr6p6-iXohJcnEPILD1eIQP2fmIffFtlQlIPOhDk8WoUa04uje__8v35WoDu7tHiSkTZ1jJsdLfFYCOn16DU9u-NpaEnUFJGMWiIJaHh63B2CWaErIqTgd8UYZpH4AghAjllHZY5FN-cfKw0TeOj9WacWA63mwbqV_GjbTnjtZ6rwBbkV8FJjP8j1Q6ZjGO5exx4mfV6So3TaBqtUlJUOxXGew08INCV2UN9OBTUiUS9iTbgyvxwHYNZ5WXcSjWaUWOxtY4Aec5S-xbkMMRg4y0CQnx605j6Dqmgmgh6x4yTaQwTBysg54evj4RC8S-1uTVVTw8ag38Y3R6nK8j63kBttVmhkF_5IsuDn0zB7HFj9LS1Vgaw_STLM_wmKlUoM_o9wOLKHoVPZq2m8mezHsHW0z4doEwnMLEFTTSVMtzKPtCnPXAPQ5EGGsDo8HeawHu-W3G3lyxp62NOLLZSLAs5Uz5RTavwmnf3OaAYpkR4vs8Kj5Yd0RgZcfwGi7cnUJu1tVUSIqel4pLEDVZj7IaZIZX0smaroyQoc_Z9p9Ctz0waPD5-nafQSlp1uT8IBNoJh3ANBZE97okIdhUOXwweRlw--Ew0D31rCtSiaWwt1PZ5cvq2ayNYmQzI4b9-deqIjvhxoV35ka9TmmlZDM49uWq_LhseoPElt2xgzIIPxybEyKG7mkNHuMz_67CPeX7aNFI9scdGIBajC3PecSAtvm60iQw0BAaPRd3pADrfVSk0it3DSudjyKXocYceYtT1lAKKDZfZcpgIVJQCWFq5wnK4a0JnIBlwgViJWTvyH00waieet-4nfXRH_oxLU6k5KYEnMbYEWoR118sdW_fqRvsna-OiHGuYQpWgD84cGWmDn_QFXLX7PcYTcHyt289qrn42N2iNm9Kjf3-uAgIvCVkoeR_45qEGMnhO0Q0YrGr6ylhRntLZ_BXtPAiopzoA-rWXUibawo8DJlN27J3EIQ2Efn9vTA4iK2Gex58bVjxMLz_sGHNJK0u4UBnp4Pp0NtPvTaEIsMAs6HTM9NH9cBVmYJ8gplb7iySi-cCjqTlHnv6E-DBQD8w5oXtcR54rpvxCBXjKq7Gtb88PiPNIjT6vR9qGC_WQhVlXr-ZswgXs0tQNZpMPR1Dxb0vLpkc-TZ1c0nVEBzLhfSo_oYn60_61yp76G9-dzWr6b0dsOzrMZa3DaqtE-_pZoS2qndAD8skDWOzfmk2in_X_8PweYmp7FbIoX-2pG0gg23F1MjL86-J8qspXKABiIzhtgGeNWirWOsXflw6-fut8VUM0t5-dXCw4WBWAPDuCLUtUXeS5zBPfZ8kd8XLsYFt1Aci3Qu5TpD7UFWMyhooxEtSP1GtrDlsC7w_hNAAgIo-OBjRJB5Fv3uCZt0E47q_ZMaXERTf_nXubmNMMg_fmpQbSCc-_wphba1DSF0Gy8gI-zezxatl8ml3dWMwMx0YzHq06v416ANYlofTPKQmsJ5bp9xHO1p7i2PjdPkE0uO6PHNUYBmDcLHJspBQSlJbLwjPgsGj-ecWcs8nrE7GxGcLXAMK4fX-nrr0fwhYI9O_DwqUxf8sLV4yVVaXQHzDzlHfiDxWJMkDr9AYEeGgSCkHRlVOmTljGf_8tZ_fmYA2zyPYhYYlVe-UKE_qPPW6F24n-YzJV9CWXHXEJ74zlX73n8SDHDJjNQdSx0wFwe2nCE'
        self.resource_uri = 'https://testflask.halopsa.com/api'
        self.authorisation_uri = 'https://uk-trial.halopsa.com/token?tenant=testflask'


    def auth(self):
        payload = 'grant_type=client_credentials&client_id=99a1a784-ca7d-4275-aa5a-c9ac3b6f239b&client_secret=f4fb1a4d-8556-4b08-9662-18c9c36f6cf6-9e4f4bc1-5e5c-4384-8cb7-3b84684f6a8d'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

        response = requests.request("POST", self.authorisation_uri, headers=headers, data=payload)
        self.bearer = response.access_token


    def getTickets(self):
        payload = {}
        headers = {
            'Authorization': 'Bearer ' + self.bearer
        }

        response = requests.request("GET", self.resource_uri + '/tickets', headers=headers, data=payload)

        #print(response.text)
        return response.status_code


    def getTicket(self, id):
        pass

    def postTicket(self, data):

        payload = json.dumps([
            data])
        headers = {
            'Authorization': 'Bearer ' + self.bearer,
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.resource_uri + '/tickets', headers=headers, data=payload)
        print(response.text)
        return response.text

    def deleteTicket(self, id):
        pass


class halo_customer:

    def __init__(self):
        self.endpoint = "dgyueiw"
