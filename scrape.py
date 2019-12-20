#!/usr/bin/env python3

from requests_html import HTMLSession

def sgb_fss_generate_seed_urls():
    seed_urls = []
    # for lang in ["de", "fr", "it"]:
    #     for i in 'abcdefghijklmnopqrstuvwxyz':
    #         for j in 'abcdefghijklmnopqrstuvwxyz':
    #             seed_urls += [
    #                 "https://signsuisse.sgb-fss.ch/fr/index.php"+
    #                 "?eID=signsuisse_search&sword={}&lang={}&curlang={}"
    #                 .format(i+j, lang, lang)
    #             ]

    session = HTMLSession()
    r = session.get("https://signsuisse.sgb-fss.ch/fr/recherche-par-configuration-forme-de-la-main/")

    # ids = []
    # for elem in r.html.find(".stufe1 .handform"):
    #     ids += [elem.attrs['data-handformuid']]
    # for id in ids:
    #     seed_urls += [
    #         "https://signsuisse.sgb-fss.ch/index.php?id=32&"+
    #         "tx_issignsuisselexikon_anzeige[action]=ajaxsearch&"+
    #         "tx_issignsuisselexikon_anzeige[controller]=Gebaerden&"+
    #         "type=6666&tx_issignsuisselexikon_anzeige[stufe]=1&"+
    #         "tx_issignsuisselexikon_anzeige[categories]={}&L=1".format(id)
    #     ]

    ids = []
    for elem in r.html.find(".stufe3 .handform"):
        ids += [elem.attrs['data-handformuid']]
    for id in ids:
        seed_urls += [
            "https://signsuisse.sgb-fss.ch/index.php?id=32&"+
            "tx_issignsuisselexikon_anzeige[action]=ajaxsearch&"+
            "tx_issignsuisselexikon_anzeige[controller]=Gebaerden&"+
            "type=6666&tx_issignsuisselexikon_anzeige[stufe]=2&"+
            "tx_issignsuisselexikon_anzeige[categories]={}&L=1".format(id)
        ]

    return seed_urls


if __name__ == "__main__":
    seed_urls = [
        "https://signsuisse.sgb-fss.ch/",
    ]
    seed_urls += sgb_fss_generate_seed_urls()
    # print(seed_urls)

    session = HTMLSession()
    for url in seed_urls:
        r = session.get(url)
        print(r.html.absolute_links)
