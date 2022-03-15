param(  
    [string]$ResultFile="Resultados.txt",
    [string]$ResultFile1="Resultados1.txt",
    [string]$ResultFile2="Resultados2.txt"
)

$status = (Invoke-WebRequest https://discuss.zerotier.com).StatusCode
$statusdes = (Invoke-WebRequest https://discuss.zerotier.com).StatusDescription
if ( ($status = 200) -and ($statusdes = "OK"))
{
	$j = (Invoke-WebRequest https://discuss.zerotier.com).content | Select-Object $j | Format-Table -HideTableHeaders | Out-File $ResultFile -Encoding ascii
	$s = (Invoke-WebRequest https://discuss.zerotier.com).rawcontent | Select-Object $s | Format-Table -HideTableHeaders | Out-File $ResultFile1 -Encoding ascii
	$k = Invoke-RestMethod https://discuss.zerotier.com -Method GET | Select-Object $k | Format-Table -HideTableHeaders | Out-File $ResultFile2 -Encoding ascii
}
