---
title: "Sử dụng git bundle để tải mã nguồn I2P"
description: "Sao chép các repository lớn qua I2P sử dụng git bundles và BitTorrent"
slug: "git-bundle"
lastUpdated: "2020-09"
accurateFor: "0.9.47"
---

Việc sao chép các kho phần mềm lớn qua I2P có thể khó khăn, và việc sử dụng git đôi khi có thể làm cho việc này trở nên khó khăn hơn. May mắn thay, đôi khi nó cũng có thể làm cho việc này dễ dàng hơn. Git có lệnh `git bundle` có thể được sử dụng để biến một kho git thành một tệp mà git sau đó có thể clone, fetch, hoặc import từ một vị trí trên đĩa cục bộ của bạn. Bằng cách kết hợp khả năng này với các lần tải xuống bittorrent, chúng ta có thể giải quyết các vấn đề còn lại với `git clone`.

---

## Trước khi Bắt đầu

Nếu bạn có ý định tạo một git bundle, bạn **phải** đã sở hữu một bản sao đầy đủ của kho **git**, không phải kho mtn. Bạn có thể lấy nó từ github hoặc từ git.idk.i2p, nhưng một shallow clone (một bản clone được thực hiện với --depth=1) *sẽ không hoạt động*. Nó sẽ thất bại một cách âm thầm, tạo ra thứ trông giống như một bundle, nhưng khi bạn cố gắng clone nó thì sẽ thất bại. Nếu bạn chỉ đang tải về một git bundle đã được tạo sẵn, thì phần này không áp dụng cho bạn.

---

## Tải mã nguồn I2P qua Bittorrent

Ai đó sẽ cần cung cấp cho bạn một tệp torrent hoặc magnet link tương ứng với một `git bundle` hiện có mà họ đã tạo sẵn cho bạn. Một bundle gần đây được tạo đúng cách của mã nguồn i2p.i2p chính thức tính đến thứ Tư, ngày 18 tháng 3 năm 2020, có thể tìm thấy bên trong I2P tại pastebin của tôi paste.idk.i2p/f/4hq37i.

Khi đã có bundle, bạn sẽ cần sử dụng git để tạo một repository hoạt động từ nó. Nếu bạn đang sử dụng GNU/Linux và i2psnark, git bundle sẽ được đặt tại $HOME/.i2p/i2psnark hoặc, như một dịch vụ trên Debian, /var/lib/i2p/i2p-config/i2psnark. Nếu bạn đang sử dụng BiglyBT trên GNU/Linux, nó có thể ở "$HOME/BiglyBT Downloads/" thay thế. Các ví dụ ở đây giả định I2PSnark trên GNU/Linux, nếu bạn sử dụng thứ gì khác, hãy thay thế đường dẫn tới bundle bằng thư mục tải xuống được ưa thích bởi client và nền tảng của bạn.

### Sử dụng `git clone`

Sao chép từ git bundle rất dễ, chỉ cần:

```
git clone $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
Nếu bạn gặp lỗi sau đây, hãy thử sử dụng git init và git fetch thủ công thay thế.

```
fatal: multiple updates for ref 'refs/remotes/origin/master' not allowed
```
### Sử dụng `git init` và `git fetch`

Trước tiên, tạo một thư mục i2p.i2p để biến thành kho lưu trữ git.

```
mkdir i2p.i2p && cd i2p.i2p
```
Tiếp theo, khởi tạo một repository git trống để fetch các thay đổi trở lại.

```
git init
```
Cuối cùng, tải repository từ bundle.

```
git fetch $HOME/.i2p/i2psnark/i2p.i2p.bundle
```
### Thay thế remote bundle bằng remote upstream

Bây giờ bạn đã có một bundle, bạn có thể theo dõi các thay đổi bằng cách đặt remote tới nguồn repository upstream.

```
git remote set-url origin git@127.0.0.1:I2P_Developers/i2p.i2p
```
---

## Tạo Bundle

Đầu tiên, hãy làm theo [Hướng dẫn Git cho Người dùng](/docs/applications/git/) cho đến khi bạn có một bản sao `--unshallow` thành công của repository i2p.i2p. Nếu bạn đã có sẵn một bản sao, hãy đảm bảo chạy `git fetch --unshallow` trước khi tạo gói torrent.

Khi bạn đã có điều đó, chỉ cần chạy ant target tương ứng:

```
ant git-bundle
```
và sao chép bundle thu được vào thư mục tải xuống I2PSnark của bạn. Ví dụ:

```
cp i2p.i2p.bundle* $HOME/.i2p/i2psnark/
```
Trong một hoặc hai phút, I2PSnark sẽ phát hiện torrent. Nhấp vào nút "Start" để bắt đầu seed torrent.
