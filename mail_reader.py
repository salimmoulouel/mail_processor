import imapclient
import pprint
imapObj = imapclient.IMAPClient('outlook.office365.com', ssl=True)
imapObj.login('salimmouloueletude@outlook.fr', 'Smoul25082015')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2019'])

pprint.pprint(imapObj.select_folder('INBOX', readonly=True))

imapObj.search(['Seen']) 

imapObj.search(['SINCE 01-Jan-2019'])

UIDs = imapObj.search('SEEN')


rawMessages = imapObj.fetch(UIDs[:1], ['BODY[]'])

pprint.pprint(rawMessages)

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[3][b'BODY[]'])


message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')

message.get_addresses('bcc')


print(message.text_part.get_payload().decode(message.text_part.charset))

