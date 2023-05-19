[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/uelKf0-p)
# Kütüphane Otomasyonu Projesi
Bu proje C# programlama dili ve veritabanı yönetim sistemi olarak MySQL kullanılarak geliştirilmiş bir kütüphane otomasyonu sistemidir. Bu sistem, kütüphane yöneticileri tarafından kullanılarak kitapları, yazarları, yayınevlerini ve kullanıcıları yönetmelerine olanak sağlar.

# Proje Hazırlanış Adımları

## Gerekli yazılım ve araçlar:

- Visual Studio 2019 veya daha yeni bir sürümü

- MySQL veritabanı yönetim sistemi

- MySQL Connector/NET veritabanı bağlantı aracı

# Kullanım:

- Proje Visual Studio'da açılmalıdır.

- Veritabanı bağlantısı yapılmalıdır:

- App.config dosyası açılmalıdır.

- ConnectionStrings etiketi altındaki connectionString özelliği değiştirilmelidir. 

Örneğin:
```
<add name="KutuphaneContext" connectionString="server=localhost;
port=3306;
database=kutuphane;
uid=root;
password=123456" 
providerName="MySql.Data.MySqlClient"/>

```
# Proje Adımları:

1.Gerekli araçların Yüklenmesi: Projenin geliştirilmesi için Visual Studio IDE ve .NET Framework SDK'nın yüklü olması gerekmektedir. Bu araçlar, proje dosyalarının oluşturulması, kodlama işlemlerinin gerçekleştirilmesi ve projenin derlenmesi için kullanılacaktır.

2.Proje tasarımı için gereksinimlerin Belirlenmesi: Bu adımda, proje için gerekli özellikleri ve işlevleri belirleyin. Hangi sınıfların oluşturulacağı, hangi veritabanı işlemlerinin gerçekleştirileceği ve kullanıcı arayüzü tasarımı gibi detaylar belirlenecektir.

3.Veritabanı tasarımı: Projenin gerekli veritabanı tabloları oluşturulmalıdır. Bu tablolar, kitaplar, yazarlar, yayınevleri ve kullanıcılar gibi kütüphane öğelerini temsil etmelidir. Ayrıca, veritabanı tablolarının ilişkileri de belirlenmelidir.

4.Projenin temel kodun: Veritabanı bağlantısını ve temel işlevleri içeren sınıfları oluşturulacaktır. "KutuphaneContext" sınıfı, veritabanı işlemlerinin gerçekleştirileceği ana sınıftır.

5.Sınıfların detaylı kodları: Kitaplar, yazarlar, yayınevleri ve kullanıcılar gibi sınıfların kodlarını ayrıntılı olarak yazılacaktır. Bu kodlar, sınıfların özelliklerini ve işlevlerini içermelidir.

6.Kullanıcı arayüzünün tasarlanması: Kullanıcıların kütüphane sistemine erişebilmeleri için bir kullanıcı arayüzü tasarlanmalıdır. Bu arayüzde, kullanıcılar kitapları arayabilir, kitapları ödünç alabilir ve kütüphane öğelerini yönetebilirler.

7.Kodun test edilmesi: Kodun doğru şekilde çalıştığından emin olmak için proje test edilecektir. Veritabanı işlemlerinin doğru şekilde gerçekleştirildiğinden emin olduktan sonra  kullanıcı arayüzü işlevleri doğru şekilde çalışıyor mu kontrol edilmelidir.

# UML Diyagramı:
Aşağıda proje için hazırlanmış UML diyagramı yer almaktadır:

![](http://www.plantuml.com/plantuml/png/bLB1QiCm3BtdAtGl-G4pGaDtAMMdd7PqOsyJK-pYo6FTsByFr2fEQ63hgTLxydjFZsn7jedpG5LFTXpXa3cVtcpmknZOVp9yLm00cmEoFP5D1XwFdUS7cPiBzso_R9fnCa_S6OF_89-mq09XSrNEH3PWZtDrnPhgfxec4yT5dBqpW85dIElGmCW9m-iisc9FtHTWn_6zTPuBLCjB0_9pGVIb0VrNmicQXhirRLqNpzOjijMbqlqk4lcUCGOjTb9MBnLVpQ-Wtd-dnrItcap0drTiEdn9NY7T6p0yeO5ZZFI_73UVNLqt8FGw9HMlKzh5AbjEhKIzY9MvA6nzS7cWNm00)


Bu diyagramda, proje için gerekli olan sınıflar ve aralarındaki ilişkiler gösterilmiştir. KutuphaneContext sınıfı, MySQL veritabanı bağlantısını yönetmek için kullanılmaktadır. Kitap, Yazar, Yayinevi ve Kullanici sınıfları, kütüphane sistemine dahil olan temel veri nesnelerini temsil etmektedir. Bu sınıflar arasındaki ilişkiler ise kitapların yazarlara, yayınevlerine ve kullanıcılara ait olabileceğini göstermektedir.

# Hazırlayan:

Mehmet KESİMALİOĞLU

202503211











