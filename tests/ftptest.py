import ftplib
session = ftplib.FTP('server.address.com','USERNAME','PASSWORD')
file = open('test_image.jpg','rb')                  # file to send
session.storbinary('test_image.jpg', file)     # send the file
file.close()                                    # close file and FTP
session.quit()