param(  
    [string]$ResultFile="Resultado_de_ipconfig_displaydns.txt"

)
$j = (ipconfig /displaydns) | Select-Object $j | Format-Table -HideTableHeaders | Out-File $ResultFile -Encoding ascii

