import automationCheckIn
import automationHappyFaceBlueSight
import config_cognos
import password_handler


def main():
    password = password_handler.password_test(hash_key=config_cognos.password_hash)
    try:
        automationCheckIn.check_in(password, headless=True)
        print('Check-In Done')
    except: 
        print('Check In did not work')
    try:
        automationHappyFaceBlueSight.happy_face(password, headless=True)
        print('BlueSight Worked')
    except:
        print('BlueSight did not work')

if __name__=='__main__':
    main()