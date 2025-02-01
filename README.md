
# VXGrab

> [!IMPORTANT]
> This is considered scraping.
> VXUG do not like this, you can just use the torrents they provide.
> Be considerate with your data usage.

This is a script that will download from VX-UG, specifically, everything in the section you linked to.




## Usage/Examples

```bash
python3 vxgrab.py <link> <destination>
```

You can also just enter a root VXUG URL and it will download **everything**. Do note, this is around 500gb and you probably do not want this.


## Demo


```bash
└─$ python3 vxgrab.py https://vx-underground.org/Papers .
[*] Found directory: ICS SCADA
[+] Created directory: ./ICS SCADA
[*] Found directory: Duqu
[+] Created directory: ./ICS_SCADA/Duqu
[*] Found: 2015-06-10 - Kaspersky - Duqu2 Yara Rules.pdf
[*] Attempting to save in ./ICS_SCADA/Duqu/2015-06-10 - Kaspersky - Duqu2 Yara Rules.pdf
```
