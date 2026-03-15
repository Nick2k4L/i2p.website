---
title: "Quy trình Đề xuất I2P"
number: "001"
author: "str4d"
created: "2016-04-10"
lastupdated: "2017-04-07"
status: "Meta"
thread: "http://zzz.i2p/topics/1980"
toc: true
---
## Tổng quan

Tài liệu này mô tả cách thay đổi các thông số kỹ thuật của I2P, cách các đề xuất I2P hoạt động và mối quan hệ giữa các đề xuất I2P và các thông số kỹ thuật.

Tài liệu này được điều chỉnh từ quá trình đề xuất của Tor, và phần lớn nội dung dưới đây ban đầu được viết bởi Nick Mathewson.

Đây là một tài liệu thông tin.

## Động lực

Trước đây, quá trình cập nhật các thông số kỹ thuật của I2P tương đối không chính thức: chúng tôi sẽ đưa ra một đề xuất trên diễn đàn phát triển và thảo luận về các thay đổi, sau đó chúng tôi sẽ đạt được sự đồng thuận và vá các thông số kỹ thuật với các thay đổi dự thảo (không nhất thiết theo thứ tự đó), và cuối cùng chúng tôi sẽ thực hiện các thay đổi.

Điều này có một số vấn đề.

Thứ nhất, ngay cả khi quá trình cũ hiệu quả nhất, thông số kỹ thuật thường sẽ không đồng bộ với mã. Các trường hợp tồi tệ nhất là những trường hợp mà việc thực hiện bị hoãn: thông số kỹ thuật và mã có thể không đồng bộ trong một thời gian dài.

Thứ hai, rất khó để tham gia vào thảo luận, vì không phải lúc nào cũng rõ ràng哪 phần của chuỗi thảo luận là một phần của đề xuất, hoặc những thay đổi nào đối với thông số kỹ thuật đã được thực hiện. Các diễn đàn phát triển chỉ có thể truy cập được bên trong I2P, có nghĩa là các đề xuất chỉ có thể được xem bởi những người sử dụng I2P.

Thứ ba, rất dễ quên một số đề xuất vì chúng sẽ bị chôn vùi sâu trong danh sách chủ đề của diễn đàn.

## Cách thay đổi thông số kỹ thuật bây giờ

Trước tiên, ai đó viết một tài liệu đề xuất. Nó nên mô tả thay đổi cần được thực hiện chi tiết và đưa ra một số ý tưởng về cách thực hiện nó. Khi nó được phát triển đủ, nó trở thành một đề xuất.

Giống như một RFC, mỗi đề xuất nhận được một số. Không giống như RFC, các đề xuất có thể thay đổi theo thời gian và giữ cùng một số, cho đến khi chúng được chấp nhận hoặc từ chối. Lịch sử cho mỗi đề xuất sẽ được lưu trữ trong kho lưu trữ trang web của I2P.

Khi một đề xuất được lưu trữ, chúng tôi nên thảo luận về nó trên chủ đề tương ứng và cải thiện nó cho đến khi chúng tôi đạt được sự đồng thuận rằng đó là một ý tưởng tốt và nó được chi tiết đủ để thực hiện. Khi điều này xảy ra, chúng tôi thực hiện đề xuất và tích hợp nó vào thông số kỹ thuật. Do đó, thông số kỹ thuật vẫn là tài liệu chính thức cho giao thức I2P: không có đề xuất nào là tài liệu chính thức cho một tính năng đã được thực hiện.

(Quá trình này khá giống với Quá trình Cải tiến Python, với sự khác biệt chính là các đề xuất I2P được tái tích hợp vào thông số kỹ thuật sau khi thực hiện, trong khi PEP *trở thành* thông số kỹ thuật mới.)

### Thay đổi nhỏ

Vẫn ổn để thực hiện các thay đổi nhỏ trực tiếp vào thông số kỹ thuật nếu mã có thể được viết ngay lập tức, hoặc thay đổi thẩm mỹ nếu không cần thay đổi mã. Tài liệu này phản ánh ý định hiện tại của các nhà phát triển, không phải là một lời hứa vĩnh viễn để luôn sử dụng quá trình này trong tương lai: chúng tôi giữ quyền trở nên rất hào hứng và chạy đi thực hiện một cái gì đó trong một phiên hacking suốt đêm được thúc đẩy bởi caffeine hoặc M&M.

## Cách thêm đề xuất mới

Để gửi một đề xuất, đăng nó trên diễn đàn phát triển hoặc nhập một vé với đề xuất đính kèm.

Khi một ý tưởng đã được đề xuất, một bản thảo được định dạng đúng (xem dưới) tồn tại, và sự đồng thuận thô trong cộng đồng phát triển tích cực tồn tại rằng ý tưởng này xứng đáng được xem xét, các biên tập viên đề xuất sẽ chính thức thêm đề xuất.

Các biên tập viên đề xuất hiện tại là zzz và str4d.

## Những gì nên có trong một đề xuất

Mỗi đề xuất nên có một tiêu đề chứa các trường sau:

```
:author:
:created:
:thread:
:lastupdated:
:status:
```

- Trường `author` nên chứa tên của các tác giả của đề xuất này.
- Trường `thread` nên là một liên kết đến chủ đề diễn đàn phát triển nơi đề xuất này ban đầu được đăng, hoặc đến một chủ đề mới được tạo để thảo luận về đề xuất này.
- Trường `lastupdated` nên ban đầu bằng với trường `created`, và nên được cập nhật mỗi khi đề xuất được thay đổi.

Các trường sau nên được đặt khi cần thiết:

```
:supercedes:
:supercededby:
:editor:
```

- Trường `supercedes` là một danh sách các đề xuất mà đề xuất này thay thế. Những đề xuất đó nên được từ chối và có trường `supercededby` được đặt thành số của đề xuất này.
- Trường `editor` nên được đặt nếu có những thay đổi đáng kể được thực hiện đối với đề xuất này mà không thay đổi đáng kể nội dung của nó. Nếu nội dung đang được thay đổi đáng kể, hoặc một tác giả bổ sung nên được thêm, hoặc một đề xuất mới được tạo để thay thế đề xuất này.

Các trường sau là tùy chọn nhưng được khuyến nghị:

```
:target:
:implementedin:
```

- Trường `target` nên mô tả phiên bản mà đề xuất này hy vọng sẽ được thực hiện (nếu nó là Mở hoặc Đã chấp nhận).
- Trường `implementedin` nên mô tả phiên bản mà đề xuất này đã được thực hiện (nếu nó là Hoàn thành hoặc Đóng).

Nội dung của đề xuất nên bắt đầu với một phần Tổng quan giải thích về đề xuất, những gì nó làm và về trạng thái của nó.

Sau phần Tổng quan, đề xuất trở nên tự do hơn. Tùy thuộc vào độ dài và độ phức tạp, đề xuất có thể chia thành các phần như phù hợp, hoặc theo một định dạng thảo luận ngắn. Mỗi đề xuất nên chứa ít nhất các thông tin sau trước khi nó được chấp nhận, mặc dù thông tin không cần phải ở các phần có tên như vậy.

**Động lực**
: Vấn đề mà đề xuất đang cố gắng giải quyết là gì? Tại sao vấn đề này quan trọng? Nếu có nhiều cách tiếp cận có thể, tại sao lại chọn cách này?

**Thiết kế**
: Một cái nhìn tổng quan về các tính năng mới hoặc đã sửa đổi, cách các tính năng mới hoặc đã sửa đổi hoạt động, cách chúng tương tác với nhau và cách chúng tương tác với phần còn lại của I2P. Đây là phần chính của đề xuất. Một số đề xuất sẽ bắt đầu chỉ với Động lực và Thiết kế, và chờ đợi một thông số kỹ thuật cho đến khi Thiết kế似乎 đúng.

**Hậu quả về bảo mật**
: Những ảnh hưởng mà các thay đổi đề xuất có thể có đối với tính ẩn danh, mức độ hiểu biết về những ảnh hưởng này và như vậy.

**Thông số kỹ thuật**
: Một mô tả chi tiết về những gì cần được thêm vào thông số kỹ thuật của I2P để thực hiện đề xuất. Điều này nên được mô tả chi tiết như thông số kỹ thuật sẽ chứa: nó nên có thể cho các lập trình viên độc lập viết các triển khai tương thích với đề xuất dựa trên thông số kỹ thuật của nó.

**Tính tương thích**
: Các phiên bản I2P theo đề xuất có tương thích với các phiên bản không? Nếu có, tính tương thích sẽ được đạt được như thế nào? Thông thường, chúng tôi cố gắng không bỏ tính tương thích nếu có thể; chúng tôi chưa thực hiện một thay đổi "ngày cờ" kể từ tháng 3 năm 2008, và chúng tôi không muốn thực hiện một thay đổi khác.

**Triển khai**
: Nếu đề xuất sẽ khó triển khai trong kiến trúc hiện tại của I2P, tài liệu có thể chứa một số thảo luận về cách thực hiện nó. Các bản vá thực tế nên được đặt trên các nhánh monotone công khai, hoặc được tải lên Trac.

**Ghi chú về hiệu suất và khả năng mở rộng**
: Nếu tính năng sẽ có ảnh hưởng đến hiệu suất (về RAM, CPU, băng thông) hoặc khả năng mở rộng, nên có một số phân tích về mức độ ảnh hưởng này, để chúng tôi có thể tránh những hồi quy hiệu suất thực sự tốn kém, và để chúng tôi có thể tránh lãng phí thời gian vào những lợi ích không đáng kể.

**Tham khảo**
: Nếu đề xuất tham khảo các tài liệu bên ngoài, những tài liệu đó nên được liệt kê.

## Trạng thái đề xuất

**Mở**
: Một đề xuất đang được thảo luận.

**Đã chấp nhận**
: Đề xuất đã hoàn thành, và chúng tôi dự định sẽ thực hiện nó. Sau điểm này, các thay đổi thực质 đối với đề xuất nên được tránh, và được coi là một dấu hiệu của quá trình đã thất bại ở một nơi nào đó.

**Hoàn thành**
: Đề xuất đã được chấp nhận và thực hiện. Sau điểm này, đề xuất không nên được thay đổi.

**Đóng**
: Đề xuất đã được chấp nhận, thực hiện và hợp nhất vào các tài liệu thông số kỹ thuật chính. Đề xuất không nên được thay đổi sau điểm này.

**Từ chối**
: Chúng tôi sẽ không thực hiện tính năng như được mô tả ở đây, mặc dù chúng tôi có thể thực hiện một số phiên bản khác. Xem các bình luận trong tài liệu để biết chi tiết. Đề xuất không nên được thay đổi sau điểm này; để đưa ra một số phiên bản khác của ý tưởng, hãy viết một đề xuất mới.

**Bản thảo**
: Đây chưa phải là một đề xuất hoàn chỉnh; có những mảnh ghép rõ ràng bị thiếu. Xin đừng thêm bất kỳ đề xuất mới nào với trạng thái này; hãy đặt chúng trong thư mục "ý tưởng" thay vào đó.

**Cần sửa đổi**
: Ý tưởng cho đề xuất là một ý tưởng tốt, nhưng đề xuất như nó đứng có những vấn đề nghiêm trọng khiến nó không thể được chấp nhận. Xem các bình luận trong tài liệu để biết chi tiết.

**Đã chết**
: Đề xuất đã không được chạm vào trong một thời gian dài, và nó không giống như ai đó sẽ hoàn thành nó sớm. Nó có thể trở thành "Mở" lại nếu nó nhận được một người đề xuất mới.

**Cần nghiên cứu**
: Có những vấn đề nghiên cứu cần được giải quyết trước khi rõ ràng liệu đề xuất có phải là một ý tưởng tốt.

**Meta**
: Đây không phải là một đề xuất, mà là một tài liệu về các đề xuất.

**Dự trữ**
: Đề xuất này không phải là thứ chúng tôi đang dự định thực hiện, nhưng chúng tôi có thể muốn hồi sinh nó một ngày nào đó nếu chúng tôi quyết định làm một cái gì đó giống như những gì nó đề xuất.

**Thông tin**
: Đề xuất này là lời cuối cùng về những gì nó đang làm. Nó sẽ không trở thành một thông số kỹ thuật trừ khi ai đó sao chép và dán nó vào một thông số kỹ thuật mới cho một hệ thống con mới.

Các biên tập viên duy trì trạng thái chính xác của các đề xuất, dựa trên sự đồng thuận thô và sự riêng biệt của họ.

## Số đề xuất

Các số từ 000 đến 099 được dành cho các đề xuất đặc biệt và meta. 100 và cao hơn được sử dụng cho các đề xuất thực tế. Các số không được tái sử dụng.

## Tham khảo

* [DEV-FORUM-PROPOSAL](http://zzz.i2p/topics/new?forum_id=7-big-topics-ideas-proposals-and-discussion)
* [TORSPEC-PROCESS](https://gitweb.torproject.org/torspec.git/tree/proposals/001-process.txt)
* [TRAC-PROPOSAL](http://trac.i2p2.i2p/newticket?summary=New%20proposal:%20&type=enhancement&milestone=n/a&component=www/i2p&keywords=review-needed)
