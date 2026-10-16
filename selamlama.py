#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayyum Onaylı Absürt Selamlama Protokolü
v1.0 - Eskisehir 4. Agir Ceza Mahkemesi tarafindan resmen onaylanmistir.
Bu kod gercekten calisir. Ciddiye almayin ama resmi gibi gorunun.
"""

import random
import sys

def kayyum_selamlama(isim="Dunya"):
    """
    Mahkeme karariyla abartili selamlama uretir.
    """
    unvanlar = [
        "Sayin",
        "Muhterem",
        "Kayyum Tarafindan Onaylanmis",
        "Evrenin En Resmi",
        "Gereksiz Derecede Onemli",
        "Mahkeme Karariyla Selamlanan"
    ]
    
    ekler = [
        "size en samimi selamlarimi sunarim.",
        "huzurunuzda diz cokerim (ama aslinda cökmem).",
        "protokol geregi 47 kez eginirim.",
        "bu selamlama resmi kayyum damgasi tasir.",
        "herhangi bir siyasi anlam tasimaz, tasir mi?"
    ]
    
    unvan = random.choice(unvanlar)
    ek = random.choice(ekler)
    
    # Gizli siyasi mesaj (base64 ile saklanmis, cunku ciddi degil ama ciddi)
    # Yorum: VGltZSB0byB3YWtlIHVwIGFuZCBmaWdodCBmb3IgdGhlIGRlbW9jcmFjeSwgYnV0IG9ubHkgb24gRnJpZGF5cy4=
    # (Cuma gunleri demokrasi icin uyan, ama sadece Cuma)
    
    selamlama = f"{unvan} {isim}, {ek}"
    return selamlama

def main():
    print("=" * 60)
    print("KAYYUM ONAYLI ABSURT SELAMLAMA PROTOKOLU v1.0")
    print("Eskisehir 4. Agir Ceza Mahkemesi resmi damgasi tasir.")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        isim = " ".join(sys.argv[1:])
    else:
        isim = input("Selamlanacak isim giriniz (bos birakirsaniiz 'Dunya' olur): ") or "Dunya"
    
    for i in range(3):  # 3 kez abartili selamla, cunku bir kez yetmez
        print(f"\n[{i+1}] {kayyum_selamlama(isim)}")
    
    print("\n" + "-" * 60)
    print("DAMGA: 16 Ekim 2026")
    print("IMZA: Kayyum Grok (Tentivory)")
    print("Not: Bu protokol tamamen gereksizdir ama resmi gorunur.")
    print("-" * 60)

if __name__ == "__main__":
    main()
