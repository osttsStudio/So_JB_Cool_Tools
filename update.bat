taskkill /F /IM mc_tools.exe
mkdir bg
move .minecraft\background.png .\bg\
move .minecraft\mc_tools.exe .\
move .minecraft\config.ini .\
move .minecraft\mc_tools.ini .\
move .minecraft\Client.exe .\
move .minecraft\PCL\* .\PCL
move .minecraft\PCL\Pictures\background.png .\PCL\Pictures
echo Update is successful.