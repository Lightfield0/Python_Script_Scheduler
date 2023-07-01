# Python Script Scheduler

Bu program, kullanıcıdan birden çok Python dosyası seçmeyi ve bu dosyaları belirli bir aralıkla otomatik olarak çalıştırmayı sağlar. Ayrıca MySQL host adresi girilebilir ve kaydedilebilir.

## Kullanım

Programın ana arayüzünde birkaç bölüm bulunur:

1. **Python dosyalarını seçin:** Bu bölümde, 'Göz At' butonunu tıkladığınızda bir dosya seçici açılır ve istediğiniz Python dosyalarını seçebilirsiniz.

2. **Her dosya için saat aralığını belirleyin (saniye cinsinden):** Bu bölüm, her seçili Python dosyası için bir giriş kutusu oluşturur. Her giriş kutusuna, ilgili Python dosyasının kaç saniyede bir çalıştırılacağını girin.

3. **MySQL Host Adresi Girin:** MySQL host adresini girin ve 'Host Kaydet' butonuna tıklayarak kaydedin.

Son olarak, 'Başlat' butonuna tıklayarak otomatik program çalıştırmasını başlatabilirsiniz. Tüm seçili dosyalar, belirlediğiniz aralıklarla sürekli olarak çalıştırılır.

## Kurulum

1. Bu GitHub deposunu klonlayın veya indirin.

2. Konsol veya terminalden, indirilen klasörün içine gidin.

3. Gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:

pip install -r requirements.txt

4. Son olarak, aşağıdaki komutla programı başlatın:

python script_scheduler.py
