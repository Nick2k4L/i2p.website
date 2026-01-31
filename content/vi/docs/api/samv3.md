---
title: "SAM V3"
description: "Giao thức Nhắn tin Ẩn danh Đơn giản cho các ứng dụng I2P không phải Java"
slug: "samv3"
lastUpdated: "2025-04"
accurateFor: "0.9.66"
---

SAM là một giao thức client đơn giản để tương tác với I2P. SAM là giao thức được khuyến nghị cho các ứng dụng non-Java kết nối với mạng I2P, và được hỗ trợ bởi nhiều triển khai router khác nhau. Các ứng dụng Java nên sử dụng trực tiếp các API streaming hoặc I2CP.

SAM phiên bản 3 được giới thiệu trong bản phát hành I2P 0.7.3 (tháng 5 năm 2009) và là một giao diện ổn định và được hỗ trợ. 3.1 cũng ổn định và hỗ trợ tùy chọn loại chữ ký, điều này được khuyến nghị mạnh mẽ. Các phiên bản 3.x gần đây hơn hỗ trợ các tính năng nâng cao. Lưu ý rằng i2pd hiện tại không hỗ trợ hầu hết các tính năng 3.2 và 3.3.

Các lựa chọn thay thế: [SOCKS](/docs/api/socks), [Streaming](/docs/api/streaming), [I2CP](/docs/protocol/i2cp), [BOB (đã ngưng hỗ trợ)](/docs/api/bob). Các phiên bản đã ngưng hỗ trợ: [SAM V1](/docs/api/sam), [SAM V2](/docs/api/samv2).

## Thư viện SAM Đã biết

Cảnh báo: Một số trong những phần mềm này có thể rất cũ hoặc không được hỗ trợ. Không phần mềm nào được kiểm tra, đánh giá hoặc duy trì bởi dự án I2P trừ khi có ghi chú bên dưới. Hãy tự nghiên cứu trước khi sử dụng.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Library Name</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Language</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">Version</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">STREAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">DGRAM</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:center;">RAW</th>
      <th style="border:1px solid var(--color-border); padding:0.5rem; background:var(--color-bg-secondary); text-align:left;">Site</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2psam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++, C wrapper</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2psam">github.com/i2p/i2psam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">gosam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/goSam">github.com/eyedeekay/goSam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">sam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/sam3">github.com/eyedeekay/sam3</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">onramp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Go</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/onramp">github.com/eyedeekay/onramp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">txi2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/str4d/txi2p">github.com/str4d/txi2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.socket</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.2</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/majestrate/i2p.socket">github.com/majestrate/i2p.socket</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/l-n-s/i2plib">github.com/l-n-s/i2plib</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2plib-fork</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/weko/i2plib-fork">codeberg.org/weko/i2plib-fork</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Py2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Python</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://i2pgit.org/robin/Py2p">i2pgit.org/robin/Py2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-rs</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/i2p-rs">github.com/i2p/i2p-rs</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">libsam3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/i2p/libsam3">github.com/i2p/libsam3</a><br>(Maintained by the I2P project)</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">mooni2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Lua</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/villain/mooni2p">notabug.org/villain/mooni2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">haskell-network-anonymous-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Haskell</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/solatis/haskell-network-anonymous-i2p">github.com/solatis/haskell-network-anonymous-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p-sam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://codeberg.org/diva.exchange/i2p-sam">codeberg.org/diva.exchange/i2p-sam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">node-i2p</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Javascript</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/redhog/node-i2p">github.com/redhog/node-i2p</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Jsam</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Java</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/eyedeekay/Jsam">github.com/eyedeekay/Jsam</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">I2PSharp</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.3</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/MohA39/I2PSharp">github.com/MohA39/I2PSharp</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2pdotnet</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">.Net</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">unk</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/SamuelFisher/i2pdotnet">github.com/SamuelFisher/i2pdotnet</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">i2p.rb</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Ruby</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.0</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/dryruby/i2p.rb">github.com/dryruby/i2p.rb</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">solitude</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Rust</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">WIP</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/syvita/solitude">github.com/syvita/solitude</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">Samty</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://notabug.org/acetone/samty">notabug.org/acetone/samty</a></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">bitcoin</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;">C++</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">3.1</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">yes</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem; text-align:center;">no</td>
      <td style="border:1px solid var(--color-border); padding:0.5rem;"><a href="https://github.com/bitcoin/bitcoin/blob/master/src/i2p.cpp">source (not a library, but good reference code)</a></td>
    </tr>
  </tbody>
</table>
## Bắt Đầu Nhanh

Để triển khai một ứng dụng ngang hàng cơ bản chỉ sử dụng TCP, client phải hỗ trợ các lệnh sau:

- `HELLO VERSION MIN=3.1 MAX=3.1` - Cần thiết cho tất cả các lệnh còn lại
- `DEST GENERATE SIGNATURE_TYPE=7` - Để tạo private key và destination của chúng ta
- `NAMING LOOKUP NAME=...` - Để chuyển đổi địa chỉ .i2p thành destination
- `SESSION CREATE STYLE=STREAM ID=... DESTINATION=... i2cp.leaseSetEncType=4,0` - Cần thiết cho STREAM CONNECT và STREAM ACCEPT
- `STREAM CONNECT ID=... DESTINATION=...` - Để tạo kết nối đi ra
- `STREAM ACCEPT ID=...` - Để chấp nhận kết nối đi vào

## Hướng dẫn chung cho các nhà phát triển

### Thiết kế Ứng dụng

Các phiên SAM (hoặc bên trong I2P, các tunnel pool hoặc tập hợp các tunnel) được thiết kế để tồn tại lâu dài. Hầu hết các ứng dụng chỉ cần một phiên duy nhất, được tạo khi khởi động và đóng khi thoát. I2P khác với Tor, nơi các circuit có thể được tạo và loại bỏ nhanh chóng. Hãy suy nghĩ cẩn thận và tham khảo ý kiến của các nhà phát triển I2P trước khi thiết kế ứng dụng của bạn sử dụng nhiều hơn một hoặc hai phiên đồng thời, hoặc tạo và loại bỏ chúng một cách nhanh chóng. Hầu hết các mô hình đe dọa sẽ không yêu cầu một phiên riêng biệt cho mỗi kết nối.

Ngoài ra, vui lòng đảm bảo các cài đặt ứng dụng của bạn (và hướng dẫn cho người dùng về cài đặt router, hoặc cấu hình router mặc định nếu bạn tích hợp sẵn router) sẽ giúp người dùng của bạn đóng góp nhiều tài nguyên cho mạng hơn những gì họ tiêu thụ. I2P là một mạng ngang hàng, và mạng không thể tồn tại nếu một ứng dụng phổ biến khiến mạng rơi vào tình trạng tắc nghẽn thường xuyên.

### Tương thích và Kiểm thử

Các triển khai router Java I2P và i2pd là độc lập và có những khác biệt nhỏ về hành vi, hỗ trợ tính năng và cài đặt mặc định. Vui lòng kiểm tra ứng dụng của bạn với phiên bản mới nhất của cả hai router.

SAM của i2pd được bật mặc định; SAM của Java I2P thì không. Hãy cung cấp hướng dẫn cho người dùng về cách bật SAM trong Java I2P (thông qua /configclients trong bảng điều khiển router), và/hoặc cung cấp thông báo lỗi rõ ràng cho người dùng nếu kết nối ban đầu thất bại, ví dụ: "hãy đảm bảo rằng I2P đang chạy và giao diện SAM đã được bật".

Các router Java I2P và i2pd có các giá trị mặc định khác nhau cho số lượng tunnel. Giá trị mặc định của Java là 2 và của i2pd là 5. Đối với hầu hết các trường hợp có băng thông thấp đến trung bình và số lượng kết nối thấp đến trung bình, 2 hoặc 3 là đủ. Vui lòng chỉ định số lượng tunnel trong thông điệp SESSION CREATE để có hiệu suất nhất quán với các router Java I2P và i2pd. Xem bên dưới.

Để có thêm hướng dẫn cho các nhà phát triển về việc đảm bảo ứng dụng của bạn chỉ sử dụng những tài nguyên cần thiết, vui lòng xem [hướng dẫn đóng gói I2P với ứng dụng của bạn](/docs/applications/embedding).

### Các Loại Chữ Ký và Mã Hóa

I2P hỗ trợ nhiều loại chữ ký và mã hóa khác nhau. Để tương thích ngược, SAM mặc định sử dụng các loại cũ và không hiệu quả, vì vậy tất cả client nên chỉ định các loại mới hơn.

Loại chữ ký được chỉ định trong các lệnh DEST GENERATE và SESSION CREATE (cho tạm thời). Tất cả client nên đặt `SIGNATURE_TYPE=7` (Ed25519).

Loại mã hóa được chỉ định trong lệnh SESSION CREATE. Nhiều loại mã hóa được cho phép. Client nên đặt `i2cp.leaseSetEncType=4` (chỉ dành cho ECIES-X25519) hoặc `i2cp.leaseSetEncType=4,0` (cho ECIES-X25519 và ElGamal, nếu cần tính tương thích).

## Thay đổi phiên bản 3

### Thay đổi phiên bản 3.0

Phiên bản 3.0 được giới thiệu trong bản phát hành I2P 0.7.3. SAMv2 cung cấp cách quản lý nhiều socket trên cùng một I2P destination *song song*, tức là client không phải đợi dữ liệu được gửi thành công trên một socket trước khi gửi dữ liệu trên socket khác. Nhưng tất cả dữ liệu đều truyền qua cùng một socket client-to-SAM, điều này khá phức tạp để client quản lý.

SAM v3 quản lý socket theo cách khác: mỗi *I2P socket* tương ứng với một socket client-to-SAM duy nhất, điều này đơn giản hơn nhiều để xử lý. Điều này tương tự như [BOB](/docs/api/bob).

SAMv3 cũng cung cấp một cổng UDP để gửi datagram qua I2P, và có thể chuyển tiếp các datagram I2P trở lại máy chủ datagram của client.

### Thay đổi phiên bản 3.1

Phiên bản 3.1 được giới thiệu trong bản phát hành Java I2P 0.9.14 (tháng 7 năm 2014). SAMv3.1 là phiên bản SAM tối thiểu được khuyến nghị vì hỗ trợ các loại chữ ký tốt hơn so với SAMv3.0. i2pd cũng hỗ trợ hầu hết các tính năng của phiên bản 3.1.

- DEST GENERATE và SESSION CREATE hiện đã hỗ trợ tham số SIGNATURE_TYPE.
- Các tham số MIN và MAX trong HELLO VERSION hiện là tùy chọn.
- Các tham số MIN và MAX trong HELLO VERSION hiện hỗ trợ các phiên bản một chữ số như "3".
- RAW SEND hiện đã được hỗ trợ trên bridge socket.

### Thay đổi phiên bản 3.2

Phiên bản 3.2 đã được giới thiệu trong bản phát hành Java I2P 0.9.24 (tháng 1 năm 2016). Lưu ý rằng i2pd hiện tại không hỗ trợ hầu hết các tính năng của 3.2.

#### Hỗ trợ Cổng và Giao thức I2CP

- SESSION CREATE tùy chọn FROM_PORT và TO_PORT
- SESSION CREATE STYLE=RAW tùy chọn PROTOCOL
- STREAM CONNECT, DATAGRAM SEND, và RAW SEND tùy chọn FROM_PORT và TO_PORT
- RAW SEND tùy chọn PROTOCOL
- DATAGRAM RECEIVED, RAW RECEIVED, và các stream được chuyển tiếp hoặc nhận cùng các datagram có thể trả lời, bao gồm FROM_PORT và TO_PORT
- Tùy chọn RAW session HEADER=true sẽ làm cho các raw datagram được chuyển tiếp có thêm một dòng chứa PROTOCOL=nnn FROM_PORT=nnnn TO_PORT=nnnn ở phía trước
- Dòng đầu tiên của datagram được gửi qua port 7655 giờ có thể bắt đầu với bất kỳ phiên bản 3.x nào
- Dòng đầu tiên của datagram được gửi qua port 7655 có thể chứa bất kỳ tùy chọn nào trong số FROM_PORT, TO_PORT, PROTOCOL
- RAW RECEIVED bao gồm PROTOCOL=nnn

#### SSL và Xác thực

- USER/PASSWORD trong các tham số HELLO để ủy quyền. Xem [bên dưới](#authorization).
- Cấu hình ủy quyền tùy chọn với lệnh AUTH. Xem [bên dưới](#authorization-configuration-sam-32-or-higher-optional-feature).
- Hỗ trợ SSL/TLS tùy chọn trên control socket. Xem [bên dưới](#ssl).
- Tùy chọn STREAM FORWARD SSL=true

#### Đa luồng

- Các STREAM ACCEPT đang chờ xử lý đồng thời được phép trên cùng một session ID.

#### Phân Tích Dòng Lệnh và Keepalive

- Các lệnh tùy chọn QUIT, STOP và EXIT để đóng phiên làm việc và socket. Xem [bên dưới](#quitstopexitinvisible-sam-32-or-higher-optional-features).
- Phân tích cú pháp lệnh sẽ xử lý đúng UTF-8
- Phân tích cú pháp lệnh xử lý đáng tin cậy khoảng trắng bên trong dấu ngoặc kép
- Dấu gạch chéo ngược '\\' có thể thoát dấu ngoặc kép trên dòng lệnh
- Khuyến nghị rằng server ánh xạ các lệnh thành chữ hoa, để dễ dàng kiểm tra qua telnet.
- Các giá trị tùy chọn rỗng như PROTOCOL hoặc PROTOCOL= có thể được cho phép, tùy thuộc vào implementation.
- PING/PONG cho keepalive. Xem bên dưới.
- Các server có thể triển khai timeout cho HELLO hoặc các lệnh tiếp theo, tùy thuộc vào implementation.

### Thay đổi phiên bản 3.3

Phiên bản 3.3 được giới thiệu trong Java I2P phiên bản 0.9.25 (tháng 3 năm 2016). Lưu ý rằng i2pd hiện tại không hỗ trợ hầu hết các tính năng 3.3.

- Cùng một session có thể được sử dụng đồng thời cho streams, datagrams, và raw. Các gói tin và streams đến sẽ được định tuyến dựa trên I2P protocol và to-port. Xem [phần PRIMARY bên dưới](#sam-primary-sessions-v33-and-higher).
- DATAGRAM SEND và RAW SEND hiện hỗ trợ các tùy chọn SEND_TAGS, TAG_THRESHOLD, EXPIRES, và SEND_LEASESET. Xem [phần gửi datagram bên dưới](#sending-repliable-or-raw-datagrams).

## Giao thức Phiên bản 3

### Tổng quan Đặc tả Simple Anonymous Messaging (SAM) Phiên bản 3.3

Ứng dụng client giao tiếp với SAM bridge, nó xử lý tất cả các chức năng I2P (sử dụng [thư viện streaming](/docs/api/streaming) cho các luồng ảo, hoặc [I2CP](/docs/protocol/i2cp) trực tiếp cho datagram).

Theo mặc định, giao tiếp giữa client và cầu nối SAM không được mã hóa và không xác thực. Cầu nối SAM có thể hỗ trợ kết nối SSL/TLS; chi tiết cấu hình và triển khai nằm ngoài phạm vi của đặc tả này. Kể từ SAM 3.2, các tham số xác thực user/password tùy chọn được hỗ trợ trong quá trình bắt tay ban đầu và có thể được cầu nối yêu cầu.

Các giao tiếp I2P có thể có nhiều hình thức khác biệt:

- [Luồng ảo](/docs/api/streaming)
- [Datagram có thể phản hồi và xác thực](/docs/specs/datagrams#repliable) (tin nhắn với trường FROM)
- [Datagram ẩn danh](/docs/specs/datagrams#raw) (tin nhắn ẩn danh thô)
- [Datagram2](/docs/specs/datagrams#datagram2) (định dạng mới có thể phản hồi và xác thực)
- [Datagram3](/docs/specs/datagrams#datagram3) (định dạng mới có thể phản hồi nhưng không xác thực)

Các giao tiếp I2P được hỗ trợ bởi các session I2P, và mỗi session I2P được ràng buộc với một địa chỉ (được gọi là destination). Một session I2P được liên kết với một trong ba loại trên, và không thể thực hiện các giao tiếp của loại khác, trừ khi sử dụng [PRIMARY sessions](#sam-primary-sessions-v33-and-higher).

### Mã hóa và Thoát ký tự

Tất cả các thông điệp SAM này được gửi trên một dòng duy nhất, kết thúc bằng ký tự xuống dòng (\\n). Trước SAM 3.2, chỉ hỗ trợ ASCII 7-bit. Từ SAM 3.2 trở đi, mã hóa phải là UTF-8. Bất kỳ khóa hoặc giá trị được mã hóa UTF8 nào cũng sẽ hoạt động.

Định dạng được hiển thị trong đặc tả này chỉ để dễ đọc, và trong khi hai từ đầu tiên trong mỗi thông điệp phải giữ nguyên thứ tự cụ thể, thứ tự của các cặp key=value có thể thay đổi (ví dụ "ONE TWO A=B C=D" hoặc "ONE TWO C=D A=B" đều là các cấu trúc hoàn toàn hợp lệ). Ngoài ra, giao thức này phân biệt chữ hoa chữ thường. Trong phần sau, các ví dụ thông điệp được đặt trước bằng "->" cho các thông điệp gửi từ client đến SAM bridge, và bằng "<-" cho các thông điệp gửi từ SAM bridge đến client.

Dòng lệnh hoặc phản hồi cơ bản có một trong các dạng sau:

```
COMMAND SUBCOMMAND [key=value] [key=value] ...
COMMAND                                           # As of SAM 3.2
PING[ arbitrary text]                             # As of SAM 3.2
PONG[ arbitrary text]                             # As of SAM 3.2
```
COMMAND không có SUBCOMMAND chỉ được hỗ trợ cho một số lệnh mới trong SAM 3.2.

Các cặp Key=value phải được phân tách bằng một khoảng trắng duy nhất. (Kể từ SAMv3.2, nhiều khoảng trắng được cho phép) Các giá trị phải được đặt trong dấu ngoặc kép nếu chúng chứa khoảng trắng, ví dụ key="long value text". (Trước SAMv3.2, điều này không hoạt động ổn định trong một số triển khai)

Trước SAM 3.2, không có cơ chế escape. Từ SAM 3.2, dấu nháy kép có thể được escape bằng dấu gạch chéo ngược '\\' và dấu gạch chéo ngược có thể được biểu diễn bằng hai dấu gạch chéo ngược '\\\\'.

### Giá Trị Rỗng

Kể từ SAMv3.2, các giá trị tùy chọn rỗng như KEY, KEY=, hoặc KEY="" có thể được cho phép, tùy thuộc vào cách triển khai.

### Phân biệt chữ hoa chữ thường

Giao thức, như đã quy định, phân biệt chữ hoa chữ thường. Được khuyến nghị nhưng không bắt buộc là server ánh xạ các lệnh thành chữ hoa, để dễ dàng kiểm tra thông qua telnet. Điều này sẽ cho phép, ví dụ, "hello version" hoạt động. Điều này phụ thuộc vào cách triển khai. Không ánh xạ các key hoặc giá trị thành chữ hoa, vì điều này sẽ làm hỏng các tùy chọn [I2CP](/docs/protocol/i2cp).

### Quá trình bắt tay kết nối SAM

Không có giao tiếp SAM nào có thể xảy ra cho đến khi client và bridge đã thống nhất về phiên bản giao thức, điều này được thực hiện bằng cách client gửi HELLO và bridge gửi HELLO REPLY:

```
->  HELLO VERSION
          [MIN=$min]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [MAX=$max]            # Optional as of SAM 3.1, required for 3.0 and earlier
          [USER="xxx"]          # As of SAM 3.2, required if authentication is enabled, see below
          [PASSWORD="yyy"]      # As of SAM 3.2, required if authentication is enabled, see below
```
và

```
<-  HELLO REPLY RESULT=OK VERSION=3.1
```
Kể từ phiên bản 3.1 (I2P 0.9.14), các tham số MIN và MAX là tùy chọn. SAM sẽ luôn trả về phiên bản cao nhất có thể với các ràng buộc MIN và MAX được cho, hoặc phiên bản máy chủ hiện tại nếu không có ràng buộc nào được đưa ra.

Nếu cầu nối SAM không thể tìm thấy phiên bản phù hợp, nó sẽ trả lời bằng:

```
<- HELLO REPLY RESULT=NOVERSION
```
Nếu xảy ra lỗi nào đó, chẳng hạn như định dạng yêu cầu không hợp lệ, nó sẽ phản hồi với:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
#### SSL

Control socket của server có thể tùy chọn hỗ trợ SSL/TLS, tùy theo cấu hình trên server và client. Các implementation có thể cung cấp các lớp transport khác; điều này nằm ngoài phạm vi định nghĩa giao thức.

#### Ủy quyền

Để ủy quyền, client thêm USER="xxx" PASSWORD="yyy" vào các tham số HELLO. Dấu ngoặc kép cho user và password được khuyến nghị nhưng không bắt buộc. Dấu ngoặc kép bên trong user hoặc password phải được escape bằng dấu gạch chéo ngược. Khi thất bại, server sẽ phản hồi với I2P_ERROR và một thông điệp. Khuyến nghị nên bật SSL trên bất kỳ SAM server nào mà cần ủy quyền.

#### Hết thời gian chờ

Các server có thể triển khai timeout cho lệnh HELLO hoặc các lệnh tiếp theo, tùy thuộc vào cách triển khai. Các client nên gửi ngay lập tức lệnh HELLO và lệnh tiếp theo sau khi kết nối.

Nếu xảy ra timeout trước khi HELLO được nhận, bridge sẽ phản hồi bằng:

```
<- HELLO REPLY RESULT=I2P_ERROR MESSAGE="$message"
```
và sau đó ngắt kết nối.

Nếu xảy ra timeout sau khi nhận được HELLO nhưng trước lệnh tiếp theo, bridge sẽ phản hồi với:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
và sau đó ngắt kết nối.

### Cổng và Giao thức I2CP

Kể từ SAM 3.2, các cổng [I2CP](/docs/protocol/i2cp) và giao thức có thể được chỉ định bởi SAM client sender để chuyển tiếp đến [I2CP](/docs/protocol/i2cp), và SAM bridge sẽ chuyển tiếp thông tin cổng và giao thức [I2CP](/docs/protocol/i2cp) đã nhận được đến SAM client.

Đối với FROM_PORT và TO_PORT, phạm vi hợp lệ là 0-65535, và giá trị mặc định là 0.

Đối với PROTOCOL, chỉ có thể được chỉ định cho RAW, phạm vi hợp lệ là 0-255, và giá trị mặc định là 18.

Đối với các lệnh SESSION, các cổng và giao thức được chỉ định là mặc định cho phiên đó. Đối với các luồng hoặc datagram riêng lẻ, các cổng và giao thức được chỉ định sẽ ghi đè các giá trị mặc định của phiên. Đối với các luồng hoặc datagram được nhận, các cổng và giao thức được chỉ ra là như đã nhận từ [I2CP](/docs/protocol/i2cp).

#### Sự Khác Biệt Quan Trọng so với IP Chuẩn

Các cổng I2CP dành cho socket và datagram của I2P. Chúng không liên quan đến các socket cục bộ của bạn kết nối tới SAM.

- Port 0 là hợp lệ và có ý nghĩa đặc biệt.
- Các port 1-1023 không đặc biệt hoặc có đặc quyền.
- Máy chủ lắng nghe trên port 0 theo mặc định, có nghĩa là "tất cả các port".
- Client gửi đến port 0 theo mặc định, có nghĩa là "bất kỳ port nào".
- Client gửi từ port 0 theo mặc định, có nghĩa là "không xác định".
- Máy chủ có thể có một dịch vụ lắng nghe trên port 0 và các dịch vụ khác lắng nghe trên các port cao hơn. Nếu vậy, dịch vụ port 0 là mặc định, và sẽ được kết nối đến nếu socket đến hoặc port datagram không khớp với dịch vụ khác.
- Hầu hết các đích I2P chỉ có một dịch vụ chạy trên chúng, vì vậy bạn có thể sử dụng các mặc định và bỏ qua cấu hình port I2CP.
- Cần SAM 3.2 hoặc 3.3 để chỉ định các port I2CP.
- Nếu bạn không cần các port I2CP, bạn không cần SAM 3.2 hoặc 3.3; 3.1 là đủ.
- Protocol 0 là hợp lệ và có nghĩa là "bất kỳ protocol nào". Điều này không được khuyến nghị và có thể sẽ không hoạt động.
- Các socket I2P được theo dõi bằng ID kết nối nội bộ. Do đó, không có yêu cầu rằng bộ 5 dest:port:dest:port:protocol phải duy nhất. Ví dụ, có thể có nhiều socket với cùng port giữa hai đích. Client không cần phải chọn "port trống" cho kết nối đi ra.

Nếu bạn đang thiết kế một ứng dụng SAM 3.3 với nhiều subsession, hãy suy nghĩ cẩn thận về cách sử dụng port và giao thức một cách hiệu quả. Xem đặc tả [I2CP](/docs/protocol/i2cp) để biết thêm thông tin.

### Phiên SAM

Một phiên SAM được tạo khi client mở một socket tới SAM bridge, thực hiện bắt tay, và gửi thông điệp SESSION CREATE, và phiên sẽ kết thúc khi socket bị ngắt kết nối.

Mỗi I2P Destination đã đăng ký được liên kết duy nhất với một session ID (hoặc nickname). Các session ID, bao gồm cả subsession ID cho các phiên PRIMARY, phải là duy nhất toàn cục trên máy chủ SAM. Để ngăn ngừa khả năng xung đột ID với các client khác, thực hành tốt nhất là client tạo ID một cách ngẫu nhiên.

Mỗi phiên được liên kết duy nhất với:

- socket mà client tạo session từ đó
- ID của nó (hoặc nickname)

#### Yêu cầu Tạo Session

Thông điệp tạo phiên làm việc chỉ có thể sử dụng một trong những dạng này (các thông điệp nhận được thông qua các dạng khác sẽ được trả lời bằng thông báo lỗi):

```
->  SESSION CREATE
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, for DESTINATION=TRANSIENT only, default DSA_SHA1
          [PORT=$port]                         # Required for DATAGRAM* RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [HEADER={true,false}]                # SAM 3.2 or higher only, for STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
DESTINATION chỉ định destination nào sẽ được sử dụng để gửi và nhận tin nhắn/luồng dữ liệu. $privkey là mã hóa base 64 của chuỗi nối [Destination](/docs/specs/common-structures#type_Destination) theo sau bởi [Private Key](/docs/specs/common-structures#type_PrivateKey) theo sau bởi [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), tùy chọn theo sau bởi [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), có kích thước 663 byte trở lên ở định dạng nhị phân và 884 byte trở lên ở định dạng base 64, tùy thuộc vào loại chữ ký. Định dạng nhị phân được chỉ định trong Private Key File. Xem thêm ghi chú về [Private Key](/docs/specs/common-structures#type_PrivateKey) trong phần Destination Key Generation bên dưới.

Nếu khóa riêng để ký đều là số không, phần [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature) sẽ theo sau. Offline signature chỉ được hỗ trợ cho các phiên STREAM và RAW. Offline signature không thể được tạo với DESTINATION=TRANSIENT. Định dạng của phần offline signature là:

1. Dấu thời gian hết hạn (4 byte, big endian, giây kể từ epoch, sẽ quay vòng vào năm 2106)
2. Loại sig của Transient Signing Public Key (2 byte, big endian)
3. Transient Signing Public key (độ dài theo quy định của loại transient sig)
4. Chữ ký của ba trường trên bởi offline key (độ dài theo quy định của loại destination sig)
5. Transient Signing Private key (độ dài theo quy định của loại transient sig)

Nếu destination được chỉ định là TRANSIENT, SAM bridge sẽ tạo một destination mới. Kể từ phiên bản 3.1 (I2P 0.9.14), nếu destination là TRANSIENT, tham số tùy chọn SIGNATURE_TYPE được hỗ trợ. Giá trị SIGNATURE_TYPE có thể là bất kỳ tên nào (ví dụ: ECDSA_SHA256_P256, không phân biệt chữ hoa thường) hoặc số (ví dụ: 1) được hỗ trợ bởi [Key Certificates](/docs/specs/common-structures#type_Certificate). Mặc định là DSA_SHA1, đây KHÔNG phải là thứ bạn muốn. Đối với hầu hết các ứng dụng, vui lòng chỉ định SIGNATURE_TYPE=7.

$nickname là sự lựa chọn của client. Không được phép có khoảng trắng.

Các tùy chọn bổ sung được cung cấp sẽ được chuyển đến cấu hình phiên I2P nếu không được bridge SAM diễn giải (ví dụ: outbound.length=0).

Các router Java I2P và i2pd có các giá trị mặc định khác nhau cho số lượng tunnel. Giá trị mặc định của Java là 2 và của i2pd là 5. Đối với hầu hết các ứng dụng có băng thông thấp đến trung bình và số lượng kết nối thấp đến trung bình, 2 hoặc 3 là đủ. Vui lòng chỉ định số lượng tunnel trong thông điệp SESSION CREATE để có được hiệu suất nhất quán với các router Java I2P và i2pd, sử dụng các tùy chọn ví dụ như inbound.quantity=3 outbound.quantity=3. Những tùy chọn này và các tùy chọn khác [được ghi chép trong các liên kết bên dưới](#tunnel-i2cp-and-streaming-options).

Cầu nối SAM đã được cấu hình sẵn với router mà nó sẽ giao tiếp qua I2P (tuy nhiên nếu cần thiết có thể có cách để ghi đè, ví dụ i2cp.tcp.host=localhost và i2cp.tcp.port=7654).

#### Phản hồi Tạo Phiên

Sau khi nhận được thông điệp tạo phiên, cầu nối SAM sẽ trả lời bằng một thông điệp trạng thái phiên như sau:

Nếu việc tạo thành công:

```
<-  SESSION STATUS RESULT=OK DESTINATION=$privkey
```
$privkey là base 64 của chuỗi kết nối [Destination](/docs/specs/common-structures#type_Destination) theo sau bởi [Private Key](/docs/specs/common-structures#type_PrivateKey) theo sau bởi [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), có thể theo sau bởi [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), có kích thước 663 byte trở lên ở định dạng nhị phân và 884 byte trở lên ở base 64, tùy thuộc vào loại chữ ký. Định dạng nhị phân được quy định trong Private Key File.

Nếu SESSION CREATE chứa một signing private key toàn số không và một phần [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), thì phản hồi SESSION STATUS sẽ bao gồm cùng dữ liệu với cùng định dạng. Xem phần SESSION CREATE ở trên để biết chi tiết.

Nếu nickname đã được liên kết với một phiên:

```
<-  SESSION STATUS RESULT=DUPLICATED_ID
```
Nếu destination đã được sử dụng:

```
<-  SESSION STATUS RESULT=DUPLICATED_DEST
```
Nếu đích đến không phải là khóa đích riêng hợp lệ:

```
<-  SESSION STATUS RESULT=INVALID_KEY
```
Nếu xảy ra lỗi khác:

```
<-  SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
Nếu không OK, MESSAGE nên chứa thông tin có thể đọc được để giải thích tại sao phiên không thể được tạo.

Lưu ý rằng router sẽ xây dựng tunnel trước khi phản hồi với SESSION STATUS. Điều này có thể mất vài giây, hoặc trong trường hợp khởi động router hoặc khi mạng bị nghẽn nghiêm trọng, có thể mất một phút hoặc lâu hơn. Nếu không thành công, router sẽ không phản hồi với thông báo lỗi trong vài phút. Không nên đặt timeout ngắn khi chờ phản hồi. Không nên hủy bỏ phiên trong khi quá trình xây dựng tunnel đang diễn ra và thử lại.

Các phiên SAM tồn tại và kết thúc cùng với socket mà chúng được liên kết. Khi socket bị đóng, phiên sẽ chết, và tất cả các kết nối sử dụng phiên đó cũng chết cùng lúc. Và ngược lại, khi phiên chết vì bất kỳ lý do gì, cầu nối SAM sẽ đóng socket.

### SAM Virtual Streams

Các luồng ảo được đảm bảo gửi một cách đáng tin cậy và theo thứ tự, với thông báo thất bại và thành công ngay khi có sẵn.

Streams là các socket giao tiếp hai chiều giữa hai I2P destinations, nhưng việc mở chúng phải được yêu cầu bởi một trong hai. Từ đây trở đi, các lệnh CONNECT được sử dụng bởi SAM client cho yêu cầu như vậy. Các lệnh FORWARD / ACCEPT được sử dụng bởi SAM client khi muốn lắng nghe các yêu cầu đến từ các I2P destinations khác.

### SAM Virtual Streams: CONNECT

Một client yêu cầu kết nối bằng cách:

- mở một socket mới với cầu nối SAM
- thực hiện cùng một bước bắt tay HELLO như trên
- gửi lệnh STREAM CONNECT

#### Yêu cầu Kết nối

```
-> STREAM CONNECT
         ID=$nickname
         DESTINATION=$destination
         [SILENT={true,false}]                # default false
         [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
         [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
```
Lệnh này thiết lập một kết nối ảo mới từ phiên cục bộ có ID là $nickname đến peer được chỉ định.

Đích là $destination, đây là base 64 của [Destination](/docs/specs/common-structures#type_Destination), có 516 hoặc nhiều hơn ký tự base 64 (387 hoặc nhiều hơn byte ở dạng nhị phân), tùy thuộc vào loại chữ ký.

**LƯU Ý:** Từ khoảng năm 2014 (SAM v3.1), Java I2P cũng đã hỗ trợ tên máy chủ và địa chỉ b32 cho $destination, nhưng điều này trước đây chưa được ghi chép. Tên máy chủ và địa chỉ b32 hiện đã được Java I2P hỗ trợ chính thức từ phiên bản 0.9.48. Router i2pd hỗ trợ tên máy chủ và địa chỉ b32 từ phiên bản 2.38.0 (0.9.50). Đối với cả hai router, hỗ trợ "b32" bao gồm hỗ trợ địa chỉ "b33" mở rộng cho các điểm đến được che mù.

#### Phản hồi Kết nối

Nếu SILENT=true được truyền vào, SAM bridge sẽ không gửi bất kỳ thông báo nào khác trên socket. Nếu kết nối thất bại, socket sẽ được đóng. Nếu kết nối thành công, tất cả dữ liệu còn lại đi qua socket hiện tại sẽ được chuyển tiếp từ và đến I2P destination peer đã kết nối.

Nếu SILENT=false, đây là giá trị mặc định, SAM bridge sẽ gửi một thông điệp cuối cùng tới client trước khi chuyển tiếp hoặc đóng socket:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Giá trị RESULT có thể là một trong các giá trị sau:

```
OK
CANT_REACH_PEER
I2P_ERROR
INVALID_KEY
INVALID_ID
TIMEOUT
```
Nếu RESULT là OK, tất cả dữ liệu còn lại đi qua socket hiện tại sẽ được chuyển tiếp từ và đến peer đích I2P đã kết nối. Nếu kết nối không thể thực hiện được (timeout, v.v.), RESULT sẽ chứa giá trị lỗi thích hợp (kèm theo MESSAGE có thể đọc được tùy chọn), và cầu nối SAM sẽ đóng socket.

Thời gian chờ kết nối luồng router nội bộ khoảng một phút, tùy thuộc vào cách triển khai. Không nên đặt thời gian chờ ngắn hơn khi đợi phản hồi.

### SAM Virtual Streams: ACCEPT

Một client chờ yêu cầu kết nối đến bằng cách:

- mở một socket mới với SAM bridge
- thực hiện cùng một HELLO handshake như trên
- gửi lệnh STREAM ACCEPT

#### Chấp nhận Yêu cầu

```
-> STREAM ACCEPT
         ID=$nickname
         [SILENT={true,false}]                # default false
```
Điều này làm cho phiên ${nickname} lắng nghe một yêu cầu kết nối đến từ mạng I2P. ACCEPT không được phép khi có một FORWARD đang hoạt động trên phiên.

Từ SAM 3.2 trở đi, nhiều STREAM ACCEPT đang chờ xử lý đồng thời được phép trên cùng một session ID (ngay cả với cùng port). Trước phiên bản 3.2, các accept đồng thời sẽ thất bại với lỗi ALREADY_ACCEPTING. Lưu ý: Java I2P cũng hỗ trợ ACCEPT đồng thời trên SAM 3.1, kể từ bản phát hành 0.9.24 (2016-01). i2pd cũng hỗ trợ ACCEPT đồng thời trên SAM 3.1, kể từ bản phát hành 2.50.0 (2023-12).

#### Phản Hồi Chấp Nhận

Nếu SILENT=true được truyền, cầu nối SAM sẽ không phát hành bất kỳ thông điệp nào khác trên socket. Nếu việc chấp nhận kết nối thất bại, socket sẽ bị đóng. Nếu việc chấp nhận kết nối thành công, tất cả dữ liệu còn lại đi qua socket hiện tại sẽ được chuyển tiếp từ và đến đích I2P được kết nối. Để đảm bảo độ tin cậy và nhận được đích cho các kết nối đến, khuyến nghị sử dụng SILENT=false.

Nếu SILENT=false, đây là giá trị mặc định, SAM bridge sẽ trả lời với:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Giá trị RESULT có thể là một trong những giá trị sau:

```
OK
I2P_ERROR
INVALID_ID
```
Nếu kết quả không phải là OK, socket sẽ bị đóng ngay lập tức bởi cầu nối SAM. Nếu kết quả là OK, cầu nối SAM bắt đầu chờ một yêu cầu kết nối đến từ một peer I2P khác. Khi một yêu cầu đến, cầu nối SAM chấp nhận nó và:

Nếu SILENT=true được truyền, SAM bridge sẽ không gửi bất kỳ thông điệp nào khác trên socket client. Tất cả dữ liệu còn lại đi qua socket hiện tại sẽ được chuyển tiếp từ và đến I2P destination peer đã kết nối.

Nếu SILENT=false được truyền vào, đây là giá trị mặc định, cầu nối SAM sẽ gửi cho client một dòng ASCII chứa khóa đích công khai base64 của peer đang yêu cầu, và thông tin bổ sung chỉ dành cho SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Sau dòng kết thúc bằng '\\n' này, tất cả dữ liệu còn lại đi qua socket hiện tại sẽ được chuyển tiếp từ và đến I2P destination peer đã kết nối, cho đến khi một trong các peer đóng socket.

#### Lỗi Sau OK

Trong một số trường hợp hiếm hoi, SAM bridge có thể gặp lỗi sau khi gửi RESULT=OK, nhưng trước khi một kết nối đến và gửi dòng $destination tới client. Các lỗi này có thể bao gồm router tắt máy, router khởi động lại, và đóng phiên. Trong những trường hợp này, khi SILENT=false, SAM bridge có thể (nhưng không bắt buộc phải - tùy thuộc vào implementation) gửi dòng:

```
<-  STREAM STATUS
         RESULT=I2P_ERROR
         [MESSAGE=...]
```
trước khi đóng socket ngay lập tức. Dòng này tất nhiên không thể giải mã được như một destination Base 64 hợp lệ.

### SAM Virtual Streams: FORWARD

Một client có thể sử dụng socket server thông thường và chờ các yêu cầu kết nối đến từ I2P. Để làm điều này, client phải:

- mở một socket mới với cầu nối SAM
- truyền cùng một bắt tay HELLO như trên
- gửi lệnh forward

#### Yêu cầu chuyển tiếp

```
-> STREAM FORWARD
         ID=$nickname
         PORT=$port
         [HOST=$host]
         [SILENT={true,false}]                # default false
         [SSL={true,false}]                   # SAM 3.2 or higher only, default false
```
Điều này làm cho phiên ${nickname} lắng nghe các yêu cầu kết nối đến từ mạng I2P. FORWARD không được phép trong khi có ACCEPT đang chờ xử lý trên phiên.

#### Chuyển tiếp phản hồi

SILENT mặc định là false. Dù SILENT là true hay false, SAM bridge luôn trả lời bằng một thông báo STREAM STATUS. Lưu ý rằng đây là hành vi khác với STREAM ACCEPT và STREAM CONNECT khi SILENT=true. Thông báo STREAM STATUS là:

```
<-  STREAM STATUS
         RESULT=$result
         [MESSAGE=...]
```
Giá trị RESULT có thể là một trong các giá trị sau:

```
OK
I2P_ERROR
INVALID_ID
```
$host là tên máy chủ hoặc địa chỉ IP của socket server mà SAM sẽ chuyển tiếp các yêu cầu kết nối. Nếu không được cung cấp, SAM sẽ lấy địa chỉ IP của socket đã đưa ra lệnh forward.

$port là số hiệu cổng của socket server mà SAM sẽ chuyển tiếp các yêu cầu kết nối đến. Đây là thông số bắt buộc.

Khi một yêu cầu kết nối đến từ I2P, cầu nối SAM sẽ mở một kết nối socket tới $host:$port. Nếu nó được chấp nhận trong vòng chưa đầy 3 giây, SAM sẽ chấp nhận kết nối từ I2P, và sau đó:

Nếu SILENT=true được truyền, tất cả dữ liệu đi qua socket hiện tại thu được sẽ được chuyển tiếp từ và đến I2P destination ngang hàng đã kết nối.

Nếu SILENT=false được truyền vào, đây là giá trị mặc định, SAM bridge sẽ gửi trên socket thu được một dòng ASCII chứa khóa đích công khai base64 của peer đang yêu cầu, và thông tin bổ sung chỉ dành cho SAM 3.2:

```
$destination
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
```
Sau dòng kết thúc bằng '\\n' này, tất cả dữ liệu còn lại đi qua socket sẽ được chuyển tiếp từ và đến I2P destination ngang hàng đã kết nối, cho đến khi một trong hai bên đóng socket.

Từ SAM 3.2, nếu SSL=true được chỉ định, socket chuyển tiếp sẽ qua SSL/TLS.

Router I2P sẽ ngừng lắng nghe các yêu cầu kết nối đến ngay khi socket "forwarding" bị đóng.

### SAM Datagrams

SAMv3 cung cấp các cơ chế để gửi và nhận datagram qua các socket datagram cục bộ. Một số triển khai SAMv3 cũng hỗ trợ cách gửi/nhận datagram cũ của v1/v2 qua socket cầu nối SAM. Cả hai đều được ghi lại bên dưới.

I2P hỗ trợ bốn loại datagram:

- Datagram có thể trả lời và xác thực được đặt tiền tố với destination của người gửi, và chứa chữ ký của người gửi, để người nhận có thể xác minh rằng destination của người gửi không bị giả mạo, và có thể trả lời datagram. Định dạng Datagram2 mới cũng có thể trả lời và xác thực được.
- Định dạng Datagram3 mới có thể trả lời nhưng không được xác thực. Thông tin người gửi không được xác minh.
- Raw datagram không chứa destination của người gửi hoặc chữ ký.

Các cổng I2CP mặc định được định nghĩa cho cả datagram có thể trả lời và datagram thô. Cổng I2CP có thể được thay đổi cho datagram thô.

Một mẫu thiết kế giao thức phổ biến là gửi các datagram có thể phản hồi đến máy chủ, với một số định danh được bao gồm, và máy chủ phản hồi bằng một datagram thô có chứa định danh đó, để phản hồi có thể được liên kết với yêu cầu. Mẫu thiết kế này loại bỏ chi phí đáng kể của các datagram có thể phản hồi trong các phản hồi. Tất cả các lựa chọn về giao thức và cổng I2CP đều cụ thể cho ứng dụng, và các nhà thiết kế nên xem xét các vấn đề này.

Xem thêm những ghi chú quan trọng về MTU datagram trong phần bên dưới.

#### Gửi Datagram Có Thể Trả Lời hoặc Datagram Thô

Mặc dù I2P không có sẵn địa chỉ FROM, để dễ sử dụng hơn, một lớp bổ sung được cung cấp dưới dạng repliable datagrams - các thông điệp không có thứ tự và không đáng tin cậy lên đến 31744 byte bao gồm địa chỉ FROM (để lại tối đa 1KB cho phần header). Địa chỉ FROM này được SAM xác thực nội bộ (sử dụng signing key của destination để xác minh nguồn) và bao gồm tính năng ngăn chặn replay.

Kích thước tối thiểu là 1. Để có độ tin cậy gửi tốt nhất, kích thước tối đa được khuyến nghị là khoảng 11 KB. Độ tin cậy tỉ lệ nghịch với kích thước thông điệp, thậm chí có thể là theo cấp số nhân.

Sau khi thiết lập một phiên SAM với STYLE=DATAGRAM hoặc STYLE=RAW, client có thể gửi các datagram có thể trả lời hoặc datagram thô qua cổng UDP của SAM (mặc định là 7655).

Dòng đầu tiên của một datagram được gửi qua cổng này phải có định dạng như sau. Tất cả nằm trên một dòng (phân cách bằng dấu cách), được hiển thị trên nhiều dòng để rõ ràng:

```
3.0                                  # As of SAM 3.2, any "3.x" is allowed. Prior to that, "3.0" is required.
$nickname
$destination
[FROM_PORT=nnn]                      # SAM 3.2 or higher only, default from session options
[TO_PORT=nnn]                        # SAM 3.2 or higher only, default from session options
[PROTOCOL=nnn]                       # SAM 3.2 or higher only, only for RAW sessions, default from session options
[SEND_TAGS=nnn]                      # SAM 3.3 or higher only, number of session tags to send
                                     # Overrides crypto.tagsToSend I2CP session option
                                     # Default is router-dependent (40 for Java router)
[TAG_THRESHOLD=nnn]                  # SAM 3.3 or higher only, low session tag threshold
                                     # Overrides crypto.lowTagThreshold I2CP session option
                                     # Default is router-dependent (30 for Java router)
[EXPIRES=nnn]                        # SAM 3.3 or higher only, expiration from now in seconds
                                     # Overrides clientMessageTimeout I2CP session option (which is in ms)
                                     # Default is router-dependent (60 for Java router)
[SEND_LEASESET={true,false}]         # SAM 3.3 or higher only, whether to send our leaseset
                                     # Overrides shouldBundleReplyInfo I2CP session option
                                     # Default is true
\n
```
- 3.0 là phiên bản của SAM. Từ SAM 3.2 trở đi, bất kỳ phiên bản 3.x nào đều được chấp nhận.
- $nickname là id của phiên DATAGRAM sẽ được sử dụng
- Đích đến là $destination, đây là base 64 của [Destination](/docs/specs/common-structures#type_Destination), có 516 hoặc nhiều hơn ký tự base 64 (387 hoặc nhiều hơn byte ở dạng nhị phân), tùy thuộc vào loại chữ ký. **LƯU Ý:** Từ khoảng năm 2014 (SAM v3.1), Java I2P cũng đã hỗ trợ hostname và địa chỉ b32 cho $destination, nhưng điều này trước đây chưa được ghi chép. Hostname và địa chỉ b32 hiện được Java I2P chính thức hỗ trợ từ bản phát hành 0.9.48. router i2pd hiện tại không hỗ trợ hostname và địa chỉ b32; hỗ trợ có thể được thêm vào trong các bản phát hành tương lai.
- Tất cả các tùy chọn là cài đặt cho từng datagram, ghi đè các giá trị mặc định được chỉ định trong SESSION CREATE.
- Các tùy chọn phiên bản 3.3 SEND_TAGS, TAG_THRESHOLD, EXPIRES, và SEND_LEASESET sẽ được chuyển tới [I2CP](/docs/protocol/i2cp) nếu được hỗ trợ. Xem [đặc tả I2CP](/docs/protocol/i2cp#msg_SendMessageExpire) để biết chi tiết. Việc hỗ trợ bởi máy chủ SAM là tùy chọn, nó sẽ bỏ qua các tùy chọn này nếu không được hỗ trợ.
- dòng này được kết thúc bằng '\\n'.

Dòng đầu tiên sẽ bị SAM loại bỏ trước khi gửi dữ liệu còn lại của thông điệp đến đích được chỉ định.

Để biết phương pháp thay thế gửi datagram có thể trả lời và datagram thô, xem [DATAGRAM SEND and RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### SAM Repliable Datagrams: Nhận một Datagram

Các datagram nhận được sẽ được SAM ghi vào socket mà phiên datagram được mở từ đó, nếu PORT chuyển tiếp không được chỉ định trong lệnh SESSION CREATE. Đây là cách nhận datagram tương thích với v1/v2.

Khi một datagram đến, cầu nối sẽ chuyển nó đến client thông qua thông điệp:

```
<-  DATAGRAM RECEIVED
           DESTINATION=$destination           # See notes below for Datagram3 format
           SIZE=$numBytes
           FROM_PORT=nnn                      # SAM 3.2 or higher only
           TO_PORT=nnn                        # SAM 3.2 or higher only
           \n
       [$numBytes of data]
```
Nguồn là $destination, đây là base 64 của [Destination](/docs/specs/common-structures#type_Destination), có 516 ký tự base 64 trở lên (387 byte trở lên ở dạng nhị phân), tùy thuộc vào loại chữ ký.

Cầu nối SAM không bao giờ tiết lộ cho client các header xác thực hoặc các trường khác, chỉ tiết lộ dữ liệu mà người gửi cung cấp. Điều này tiếp tục cho đến khi session được đóng (bởi client ngắt kết nối).

#### Chuyển tiếp Datagram Thô hoặc Có thể Trả lời

Khi tạo một phiên datagram, client có thể yêu cầu SAM chuyển tiếp các thông điệp đến tới một ip:port được chỉ định. Nó thực hiện điều này bằng cách phát lệnh CREATE với các tùy chọn PORT và HOST:

```
-> SESSION CREATE
          STYLE={DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See below for DATAGRAM2/3
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          PORT=$port
          [HOST=$host]
          [FROM_PORT=nnn]                      # SAM 3.2 or higher only, default 0
          [TO_PORT=nnn]                        # SAM 3.2 or higher only, default 0
          [PROTOCOL=nnn]                       # SAM 3.2 or higher only, for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP options
```
$privkey là base 64 của phép nối [Destination](/docs/specs/common-structures#type_Destination) theo sau bởi [Private Key](/docs/specs/common-structures#type_PrivateKey) theo sau bởi [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), tùy chọn có thể theo sau bởi [Offline Signature](/docs/specs/common-structures#struct_OfflineSignature), có độ dài 884 ký tự base 64 trở lên (663 byte trở lên ở dạng nhị phân), tùy thuộc vào loại chữ ký. Định dạng nhị phân được chỉ định trong Private Key File.

Chữ ký ngoại tuyến được hỗ trợ cho các datagram RAW, DATAGRAM2, và DATAGRAM3, nhưng không dành cho DATAGRAM. Xem phần SESSION CREATE ở trên và phần DATAGRAM2/3 bên dưới để biết chi tiết.

$host là tên máy chủ hoặc địa chỉ IP của máy chủ datagram mà SAM sẽ chuyển tiếp các datagram đến. Nếu không được cung cấp, SAM sẽ lấy địa chỉ IP của socket đã phát lệnh forward.

$port là số cổng của máy chủ datagram mà SAM sẽ chuyển tiếp các datagram đến. Nếu $port không được thiết lập, các datagram sẽ KHÔNG được chuyển tiếp, chúng sẽ được nhận trên control socket theo cách tương thích v1/v2.

Các tùy chọn bổ sung được cung cấp sẽ được chuyển đến cấu hình phiên I2P nếu không được SAM bridge diễn giải (ví dụ: outbound.length=0). Những tùy chọn này [được tài liệu hóa bên dưới](#tunnel-i2cp-and-streaming-options).

Các datagram có thể trả lời được chuyển tiếp luôn có tiền tố là đích base64, ngoại trừ Datagram3, xem bên dưới. Khi một datagram có thể trả lời đến, bridge sẽ gửi đến host:port được chỉ định một gói UDP chứa dữ liệu sau:

```
$destination                       # See notes below for Datagram3 format
FROM_PORT=nnn                      # SAM 3.2 or higher only
TO_PORT=nnn                        # SAM 3.2 or higher only
\n
$datagram_payload
```
Các datagram thô được chuyển tiếp sẽ được chuyển tiếp nguyên trạng đến host:port được chỉ định mà không có tiền tố. Gói UDP chứa dữ liệu sau:

```
$datagram_payload
```
Từ SAM 3.2 trở đi, khi HEADER=true được chỉ định trong SESSION CREATE, datagram thô được chuyển tiếp sẽ được thêm tiền tố với một dòng header như sau:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
$destination là base 64 của [Destination](/docs/specs/common-structures#type_Destination), có độ dài 516 ký tự base 64 trở lên (387 byte trở lên ở dạng nhị phân), tùy thuộc vào loại chữ ký.

#### SAM Datagram Ẩn danh (Thô)

Tận dụng tối đa băng thông của I2P, SAM cho phép các client gửi và nhận datagram ẩn danh, để việc xác thực và thông tin phản hồi do chính client quyết định. Các datagram này không đáng tin cậy và không có thứ tự, và có thể lên tới 32768 byte.

Kích thước tối thiểu là 1. Để đạt độ tin cậy gửi tối ưu, kích thước tối đa được khuyến nghị là khoảng 11 KB.

Sau khi thiết lập phiên SAM với STYLE=RAW, client có thể gửi các datagram ẩn danh thông qua cầu nối SAM theo cách hoàn toàn giống như [gửi các datagram có thể trả lời](#sending-repliable-or-raw-datagrams).

Cả hai cách nhận datagram cũng đều có sẵn cho các datagram ẩn danh.

Các datagram nhận được sẽ được SAM ghi vào socket mà từ đó phiên datagram đã được mở, nếu một PORT chuyển tiếp không được chỉ định trong lệnh SESSION CREATE. Đây là cách nhận datagram tương thích với v1/v2.

```
<- RAW RECEIVED
          SIZE=$numBytes
          FROM_PORT=nnn                      # SAM 3.2 or higher only
          TO_PORT=nnn                        # SAM 3.2 or higher only
          PROTOCOL=nnn                       # SAM 3.2 or higher only
          \n
      [$numBytes of data]
```
Khi các datagram ẩn danh cần được chuyển tiếp đến một host:port nào đó, bridge sẽ gửi đến host:port đã chỉ định một thông điệp chứa dữ liệu sau:

```
$datagram_payload
```
Kể từ SAM 3.2, khi HEADER=true được chỉ định trong SESSION CREATE, datagram thô được chuyển tiếp sẽ được thêm tiền tố với một dòng header như sau:

```
FROM_PORT=nnn
TO_PORT=nnn
PROTOCOL=nnn
\n
$datagram_payload
```
Để biết phương pháp thay thế gửi datagram ẩn danh, xem [RAW SEND](#datagram-send-raw-send-v1v2-compatible-datagram-handling).

#### Datagram 2/3

Datagram 2/3 là các định dạng mới được chỉ định vào đầu năm 2025. Hiện tại chưa có triển khai nào được biết đến. Kiểm tra tài liệu triển khai để biết trạng thái hiện tại. Xem [đặc tả kỹ thuật](/docs/specs/datagrams) để biết thêm thông tin.

Hiện tại không có kế hoạch tăng phiên bản SAM để chỉ ra hỗ trợ Datagram 2/3. Điều này có thể gây vấn đề vì các triển khai có thể muốn hỗ trợ Datagram 2/3 nhưng không hỗ trợ các tính năng SAM v3.3. Bất kỳ thay đổi phiên bản nào vẫn chưa được xác định.

Cả Datagram2 và Datagram3 đều có thể trả lời được. Chỉ có Datagram2 được xác thực.

Datagram2 hoàn toàn giống với repliable datagrams từ góc độ SAM. Cả hai đều được xác thực. Chỉ có định dạng I2CP và chữ ký là khác nhau, nhưng điều này không hiển thị với các SAM client. Datagram2 cũng hỗ trợ chữ ký ngoại tuyến, vì vậy nó có thể được sử dụng bởi các destination được ký ngoại tuyến.

Mục đích là Datagram2 sẽ thay thế Repliable datagrams cho các ứng dụng mới không yêu cầu tương thích ngược. Datagram2 cung cấp bảo vệ chống replay mà Repliable datagrams không có. Nếu cần tương thích ngược, một ứng dụng có thể hỗ trợ cả Datagram2 và Repliable trên cùng một phiên với SAM 3.3 PRIMARY sessions.

Datagram3 có thể trả lời được nhưng không được xác thực. Trường 'from' trong định dạng I2CP là một hash, không phải là một destination. $destination được gửi từ SAM server đến client sẽ là một hash base64 44-byte. Để chuyển đổi nó thành một destination đầy đủ để trả lời, hãy base64-decode nó thành 32 bytes nhị phân, sau đó base32-encode thành 52 ký tự và thêm ".b32.i2p" cho một NAMING LOOKUP. Như thường lệ, các client nên duy trì cache riêng của họ để tránh việc lặp lại NAMING LOOKUP.

Các nhà thiết kế ứng dụng nên hết sức thận trọng và cân nhắc những ảnh hưởng bảo mật của các datagram không được xác thực.

#### Các Cân nhắc về MTU Datagram V3

I2P Datagrams có thể lớn hơn MTU internet thông thường là 1500. Các datagram được gửi cục bộ và các datagram có thể trả lời được chuyển tiếp có tiền tố với destination base64 516+ byte có khả năng vượt quá MTU đó. Tuy nhiên, MTU localhost trên hệ thống Linux thường lớn hơn nhiều, ví dụ như 65536. MTU localhost sẽ khác nhau tùy theo hệ điều hành. I2P Datagrams sẽ không bao giờ lớn hơn 65536. Kích thước datagram phụ thuộc vào giao thức ứng dụng.

Nếu client SAM nằm cục bộ với server SAM và hệ thống hỗ trợ MTU lớn hơn, thì các datagram sẽ không bị phân mảnh cục bộ. Tuy nhiên, nếu client SAM ở xa, thì các datagram IPv4 sẽ bị phân mảnh và các datagram IPv6 sẽ thất bại (IPv6 không hỗ trợ phân mảnh UDP).

Các nhà phát triển thư viện client và ứng dụng nên nhận thức được những vấn đề này và tài liệu hóa các khuyến nghị để tránh phân mảnh và ngăn chặn mất gói tin, đặc biệt trên các kết nối SAM client-server từ xa.

#### DATAGRAM SEND, RAW SEND (Xử lý Datagram Tương thích V1/V2)

Trong SAMv3, cách ưa thích để gửi datagram là thông qua datagram socket tại cổng 7655 như đã được ghi chép ở trên. Tuy nhiên, các datagram có thể trả lời có thể được gửi trực tiếp qua SAM bridge socket bằng cách sử dụng lệnh DATAGRAM SEND, như đã được ghi chép trong [SAM V1](/docs/api/sam) và [SAM V2](/docs/api/samv2).

Kể từ phiên bản 0.9.14 (version 3.1), các datagram ẩn danh có thể được gửi trực tiếp thông qua socket cầu nối SAM bằng lệnh RAW SEND, như được tài liệu hóa trong [SAM V1](/docs/api/sam) và [SAM V2](/docs/api/samv2).

Kể từ phiên bản 0.9.24 (version 3.2), DATAGRAM SEND và RAW SEND có thể bao gồm các tham số FROM_PORT=nnnn và/hoặc TO_PORT=nnnn để ghi đè các cổng mặc định. Kể từ phiên bản 0.9.24 (version 3.2), RAW SEND có thể bao gồm tham số PROTOCOL=nnn để ghi đè giao thức mặc định.

Các lệnh này *không* hỗ trợ tham số ID. Các datagram được gửi đến phiên DATAGRAM- hoặc RAW-style được tạo gần đây nhất, tùy theo phù hợp. Hỗ trợ cho tham số ID có thể được thêm vào trong phiên bản tương lai.

Các định dạng DATAGRAM2 và DATAGRAM3 *không* được hỗ trợ theo cách tương thích với V1/V2.

### Phiên làm việc SAM PRIMARY (V3.3 trở lên)

*Phiên bản 3.3 được giới thiệu trong bản phát hành I2P 0.9.25.*

*Trong phiên bản trước của đặc tả này, các phiên PRIMARY được gọi là phiên MASTER. Trong cả `i2pd` và `I2P+`, chúng vẫn chỉ được biết đến là phiên MASTER.*

SAM v3.3 bổ sung hỗ trợ chạy streaming, datagrams và raw subsessions trên cùng một phiên chính, và cho phép chạy nhiều subsessions cùng kiểu. Tất cả lưu lượng subsession sử dụng một destination duy nhất, hoặc một tập hợp các tunnels. Việc định tuyến lưu lượng từ I2P dựa trên các tùy chọn port và protocol cho các subsessions.

Để tạo các subsession được ghép kênh, bạn phải tạo một session chính và sau đó thêm các subsession vào session chính. Mỗi subsession phải có một id duy nhất và một giao thức listen cùng cổng duy nhất. Các subsession cũng có thể được loại bỏ khỏi session chính.

Với một phiên PRIMARY và sự kết hợp của các phiên phụ, một SAM client có thể hỗ trợ nhiều ứng dụng, hoặc một ứng dụng phức tạp duy nhất sử dụng nhiều giao thức khác nhau, trên một bộ tunnel duy nhất. Ví dụ, một bittorrent client có thể thiết lập một phiên phụ streaming cho các kết nối peer-to-peer, cùng với các phiên phụ datagram và raw để giao tiếp DHT.

#### Tạo một Session CHÍNH

```
->  SESSION CREATE
          STYLE=PRIMARY                        # prior to 0.9.47, use STYLE=MASTER
          ID=$nickname
          DESTINATION={$privkey,TRANSIENT}
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, default 7655
          [option=value]*                      # I2CP and streaming options
```
SAM bridge sẽ phản hồi với thành công hoặc thất bại như trong [phản hồi cho SESSION CREATE tiêu chuẩn](#session-creation-response).

Không được thiết lập các tùy chọn PORT, HOST, FROM_PORT, TO_PORT, PROTOCOL, LISTEN_PORT, LISTEN_PROTOCOL, hoặc HEADER trên một phiên chính. Bạn không được phép gửi bất kỳ dữ liệu nào trên ID phiên PRIMARY hoặc trên control socket. Tất cả các lệnh như STREAM CONNECT, DATAGRAM SEND, v.v. phải sử dụng subsession ID trên một socket riêng biệt.

Phiên PRIMARY kết nối với router và xây dựng tunnel. Khi cầu nối SAM phản hồi, các tunnel đã được xây dựng và phiên sẵn sàng để thêm các phiên phụ. Tất cả các tùy chọn [I2CP](/docs/protocol/i2cp) liên quan đến các tham số tunnel như độ dài, số lượng và nickname phải được cung cấp trong SESSION CREATE của phiên chính.

Tất cả các lệnh tiện ích đều được hỗ trợ trên phiên chính.

Khi phiên chính được đóng, tất cả các phiên phụ cũng sẽ được đóng theo.

LƯU Ý: Trước phiên bản 0.9.47, sử dụng STYLE=MASTER. STYLE=PRIMARY được hỗ trợ từ phiên bản 0.9.47. MASTER vẫn được hỗ trợ để tương thích ngược.

#### Tạo một Subsession

Sử dụng cùng một control socket mà phiên PRIMARY đã được tạo trên đó:

```
->  SESSION ADD
          STYLE={STREAM,DATAGRAM,RAW,DATAGRAM2,DATAGRAM3}   # See above for DATAGRAM2/3
          ID=$nickname                         # must be unique
          [PORT=$port]                         # Required for DATAGRAM* and RAW, invalid for STREAM
          [HOST=$host]                         # Optional for DATAGRAM* and RAW, invalid for STREAM
          [FROM_PORT=nnn]                      # For outbound traffic, default 0
          [TO_PORT=nnn]                        # For outbound traffic, default 0
          [PROTOCOL=nnn]                       # For outbound traffic for STYLE=RAW only, default 18.
                                               # 6, 17, 19, 20 not allowed.
          [LISTEN_PORT=nnn]                    # For inbound traffic, default is the FROM_PORT value.
                                               # For STYLE=STREAM, only the FROM_PORT value or 0 is allowed.
          [LISTEN_PROTOCOL=nnn]                # For inbound traffic for STYLE=RAW only.
                                               # Default is the PROTOCOL value; 6 (streaming) is disallowed
          [HEADER={true,false}]                # For STYLE=RAW only, default false
          [sam.udp.host=hostname]              # Datagram bind host, Java I2P only, DATAGRAM*/RAW only, default 127.0.0.1
          [sam.udp.port=nnn]                   # Datagram bind port, Java I2P only, DATAGRAM*/RAW only, default 7655
          [option=value]*                      # I2CP and streaming options
```
Cầu nối SAM sẽ phản hồi với thành công hoặc thất bại như trong [phản hồi cho SESSION CREATE tiêu chuẩn](#session-creation-response). Vì các tunnel đã được xây dựng trong SESSION CREATE chính, cầu nối SAM sẽ phản hồi ngay lập tức.

Không đặt tùy chọn DESTINATION trên SESSION ADD. Subsession sẽ sử dụng destination được chỉ định trong session chính. Tất cả các subsession phải được thêm vào trên control socket, tức là cùng một kết nối mà bạn đã tạo session chính.

Nhiều phiên con phải có các tùy chọn đủ độc đáo để dữ liệu đến có thể được định tuyến chính xác. Cụ thể, nhiều phiên cùng loại phải có các tùy chọn LISTEN_PORT khác nhau (và/hoặc LISTEN_PROTOCOL, chỉ cho RAW). Một SESSION ADD với cổng nghe và giao thức trùng lặp với phiên con hiện có sẽ gây ra lỗi.

LISTEN_PORT là cổng I2P cục bộ, tức là cổng nhận (TO) cho dữ liệu đến. Nếu LISTEN_PORT không được chỉ định, giá trị FROM_PORT sẽ được sử dụng. Nếu LISTEN_PORT và FROM_PORT không được chỉ định, việc định tuyến đến sẽ chỉ dựa trên STYLE và PROTOCOL. Đối với LISTEN_PORT và LISTEN_PROTOCOL, 0 có nghĩa là giá trị bất kỳ, tức là ký tự đại diện. Nếu cả LISTEN_PORT và LISTEN_PROTOCOL đều là 0, phiên con này sẽ là mặc định cho lưu lượng đến không được định tuyến đến phiên con khác. Lưu lượng streaming đến (protocol 6) sẽ không bao giờ được định tuyến đến phiên con RAW, ngay cả khi LISTEN_PROTOCOL của nó là 0. Phiên con RAW không được phép đặt LISTEN_PROTOCOL là 6. Nếu không có phiên con mặc định hoặc phù hợp với protocol và cổng của lưu lượng đến, dữ liệu đó sẽ bị loại bỏ.

Sử dụng subsession ID, không phải primary session ID, để gửi và nhận dữ liệu. Tất cả các lệnh như STREAM CONNECT, DATAGRAM SEND, v.v. phải sử dụng subsession ID.

Tất cả các lệnh tiện ích đều được hỗ trợ trên phiên chính hoặc phiên phụ. Việc gửi/nhận datagram/raw v1/v2 không được hỗ trợ trên phiên chính hoặc trên các phiên phụ.

#### Dừng một Subsession

Sử dụng cùng control socket mà phiên PRIMARY đã được tạo trên đó:

```
->  SESSION REMOVE
          ID=$nickname
```
Điều này loại bỏ một subsession khỏi session chính. Không thiết lập bất kỳ tùy chọn nào khác trên SESSION REMOVE. Các subsession phải được loại bỏ trên control socket, tức là cùng một kết nối mà bạn đã tạo session chính. Sau khi một subsession được loại bỏ, nó sẽ được đóng và không thể được sử dụng để gửi hoặc nhận dữ liệu.

Cầu nối SAM sẽ phản hồi với thành công hoặc thất bại như trong [phản hồi cho SESSION CREATE tiêu chuẩn](#session-creation-response).

### Các Lệnh Tiện Ích SAM

Một số lệnh tiện ích yêu cầu phiên làm việc đã tồn tại và một số thì không. Xem chi tiết bên dưới.

#### Tra cứu Tên Máy chủ

Thông điệp sau đây có thể được sử dụng bởi client để truy vấn SAM bridge nhằm phân giải tên:

```
NAMING LOOKUP
       NAME=$name
       [OPTIONS=true]     # Default false, as of router API 0.9.66
```
được trả lời bởi

```
NAMING REPLY
       RESULT=$result
       NAME=$name
       [VALUE=$destination]
       [MESSAGE="$message"]
       [OPTION:optionkey="$optionvalue"]   # As of router API 0.9.66
```
Giá trị RESULT có thể là một trong những giá trị sau:

```
OK
INVALID_KEY
KEY_NOT_FOUND
```
Nếu NAME=ME, thì phản hồi sẽ chứa destination được sử dụng bởi session hiện tại (hữu ích nếu bạn đang sử dụng một destination TRANSIENT). Nếu $result không phải là OK, MESSAGE có thể truyền tải một thông báo mô tả, chẳng hạn như "bad format", v.v. INVALID_KEY có nghĩa là có gì đó không đúng với $name trong yêu cầu, có thể là các ký tự không hợp lệ.

$destination là base 64 của [Destination](/docs/specs/common-structures#type_Destination), có 516 ký tự base 64 trở lên (387 byte trở lên ở dạng nhị phân), tùy thuộc vào loại chữ ký.

NAMING LOOKUP không yêu cầu phải tạo session trước. Tuy nhiên, trong một số triển khai, việc tra cứu .b32.i2p chưa được cache và cần truy vấn mạng có thể thất bại, vì không có client tunnel nào khả dụng cho việc tra cứu.

#### Tùy Chọn Tra Cứu Tên

NAMING LOOKUP được mở rộng kể từ router API 0.9.66 để hỗ trợ tra cứu dịch vụ. Hỗ trợ có thể khác nhau tùy theo cách triển khai. Xem đề xuất 167 để biết thêm thông tin.

NAMING LOOKUP NAME=example.i2p OPTIONS=true yêu cầu ánh xạ tùy chọn trong phản hồi. NAME có thể là một destination base64 đầy đủ khi OPTIONS=true.

Nếu việc tra cứu destination thành công và có các tùy chọn trong leaseset, thì trong phản hồi, sau destination, sẽ có một hoặc nhiều tùy chọn ở dạng OPTION:key=value. Mỗi tùy chọn sẽ có tiền tố OPTION: riêng biệt. Tất cả các tùy chọn từ leaseset sẽ được bao gồm, không chỉ các tùy chọn bản ghi dịch vụ. Ví dụ, các tùy chọn cho các tham số được định nghĩa trong tương lai có thể xuất hiện. Ví dụ:

NAMING REPLY RESULT=OK NAME=example.i2p VALUE=base64dest OPTION:_smtp._tcp="1 86400 0 0 25 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.b32.i2p"

Các key chứa '=', và các key hoặc value chứa ký tự xuống dòng, được coi là không hợp lệ và cặp key/value sẽ bị loại bỏ khỏi phản hồi. Nếu không tìm thấy tùy chọn nào trong leaseSet, hoặc nếu leaseSet là phiên bản 1, thì phản hồi sẽ không bao gồm tùy chọn nào. Nếu OPTIONS=true có trong truy vấn, và không tìm thấy leaseSet, một giá trị kết quả mới LEASESET_NOT_FOUND sẽ được trả về.

#### Tạo Khóa Đích

Các khóa base64 công khai và riêng tư có thể được tạo ra bằng cách sử dụng thông điệp sau:

```
->  DEST GENERATE
          [SIGNATURE_TYPE=value]               # SAM 3.1 or higher only, default DSA_SHA1
```
được trả lời bởi

```
DEST REPLY
     PUB=$destination
     PRIV=$privkey
```
Kể từ phiên bản 3.1 (I2P 0.9.14), tham số tùy chọn SIGNATURE_TYPE được hỗ trợ. Giá trị SIGNATURE_TYPE có thể là bất kỳ tên nào (ví dụ: ECDSA_SHA256_P256, không phân biệt chữ hoa thường) hoặc số (ví dụ: 1) được hỗ trợ bởi [Key Certificates](/docs/specs/common-structures#type_Certificate). Mặc định là DSA_SHA1, đây KHÔNG phải là thứ bạn muốn. Đối với hầu hết các ứng dụng, vui lòng chỉ định SIGNATURE_TYPE=7.

$destination là mã base 64 của [Destination](/docs/specs/common-structures#type_Destination), có độ dài 516 hoặc nhiều hơn ký tự base 64 (387 hoặc nhiều hơn byte ở dạng nhị phân), tùy thuộc vào loại chữ ký.

$privkey là base 64 của việc nối chuỗi [Destination](/docs/specs/common-structures#type_Destination) theo sau bởi [Private Key](/docs/specs/common-structures#type_PrivateKey) theo sau bởi [Signing Private Key](/docs/specs/common-structures#type_SigningPrivateKey), có độ dài 884 ký tự base 64 trở lên (663 byte trở lên ở định dạng nhị phân), tùy thuộc vào loại chữ ký. Định dạng nhị phân được chỉ định trong Private Key File.

Ghi chú về Private Key nhị phân 256-byte: Trường này đã không được sử dụng kể từ phiên bản 0.6 (2005). Các triển khai SAM có thể gửi dữ liệu ngẫu nhiên hoặc toàn bộ số không trong trường này; đừng lo lắng về chuỗi AAAA trong base 64. Hầu hết các ứng dụng sẽ chỉ đơn giản lưu trữ chuỗi base 64 và trả về nguyên vẹn trong SESSION CREATE, hoặc giải mã thành nhị phân để lưu trữ, sau đó mã hóa lại cho SESSION CREATE. Tuy nhiên, các ứng dụng có thể giải mã base 64, phân tích nhị phân theo đặc tả PrivateKeyFile, loại bỏ phần private key 256-byte, và sau đó thay thế nó bằng 256 byte dữ liệu ngẫu nhiên hoặc toàn bộ số không khi mã hóa lại cho SESSION CREATE. TẤT CẢ các trường khác trong đặc tả PrivateKeyFile phải được bảo tồn. Điều này sẽ tiết kiệm 256 byte dung lượng hệ thống tập tin nhưng có lẽ không đáng để bận tâm đối với hầu hết các ứng dụng. Xem đề xuất 161 để biết thêm thông tin và bối cảnh.

DEST GENERATE không yêu cầu phải tạo session trước.

DEST GENERATE không thể được sử dụng để tạo một đích với chữ ký ngoại tuyến.

#### PING/PONG (SAM 3.2 trở lên)

Cả client hoặc server đều có thể gửi:

```
PING[ arbitrary text]
```
trên cổng điều khiển, với phản hồi:

```
PONG[ arbitrary text from the ping]
```
được sử dụng để duy trì kết nối socket điều khiển. Bất kỳ bên nào cũng có thể đóng phiên làm việc và socket nếu không nhận được phản hồi trong thời gian hợp lý, tùy thuộc vào cách triển khai.

Nếu xảy ra timeout khi chờ PONG từ client, bridge có thể gửi:

```
<- SESSION STATUS RESULT=I2P_ERROR MESSAGE="$message"
```
và sau đó ngắt kết nối.

Nếu xảy ra timeout khi chờ PONG từ bridge, client có thể đơn giản là ngắt kết nối.

PING/PONG không yêu cầu phải tạo session trước.

#### QUIT/STOP/EXIT (SAM 3.2 trở lên, tính năng tùy chọn)

Các lệnh QUIT, STOP và EXIT sẽ đóng phiên làm việc và socket. Việc triển khai là tùy chọn, để thuận tiện cho việc kiểm thử qua telnet. Việc có bất kỳ phản hồi nào trước khi socket được đóng (ví dụ, thông báo SESSION STATUS) là tùy thuộc vào cách triển khai và nằm ngoài phạm vi của đặc tả này.

QUIT/STOP/EXIT không yêu cầu phải tạo session trước.

#### HELP (tính năng tùy chọn)

Các server có thể triển khai lệnh HELP. Việc triển khai là tùy chọn, để dễ dàng kiểm tra qua telnet. Định dạng đầu ra và việc phát hiện kết thúc đầu ra là đặc thù của từng triển khai và nằm ngoài phạm vi của đặc tả này.

HELP không yêu cầu phải tạo session trước.

#### Cấu hình Ủy quyền (SAM 3.2 trở lên, tính năng tùy chọn)

Cấu hình ủy quyền sử dụng lệnh AUTH. Một máy chủ SAM có thể triển khai những lệnh này để hỗ trợ lưu trữ bền vững thông tin xác thực. Cấu hình xác thực bằng các phương thức khác ngoài những lệnh này là đặc thù của từng triển khai và nằm ngoài phạm vi của đặc tả này.

- AUTH ENABLE bật xác thực trên các kết nối tiếp theo
- AUTH DISABLE tắt xác thực trên các kết nối tiếp theo
- AUTH ADD USER="foo" PASSWORD="bar" thêm một người dùng/mật khẩu
- AUTH REMOVE USER="foo" xóa người dùng này

Dấu ngoặc kép cho tên người dùng và mật khẩu được khuyến nghị nhưng không bắt buộc. Dấu ngoặc kép bên trong tên người dùng hoặc mật khẩu phải được escape bằng dấu gạch chéo ngược. Khi thất bại, server sẽ phản hồi với I2P_ERROR và một thông báo.

AUTH không yêu cầu phải tạo session trước.

### Giá trị RESULT

Đây là các giá trị có thể được chứa trong trường RESULT, cùng với ý nghĩa của chúng:

```
OK              Operation completed successfully
CANT_REACH_PEER The peer exists, but cannot be reached
DUPLICATED_DEST The specified Destination is already in use
I2P_ERROR       A generic I2P error (e.g. I2CP disconnection, etc.)
INVALID_KEY     The specified key is not valid (bad format, etc.)
KEY_NOT_FOUND   The naming system can't resolve the given name
PEER_NOT_FOUND  The peer cannot be found on the network
TIMEOUT         Timeout while waiting for an event (e.g. peer answer)
LEASESET_NOT_FOUND  See Name Lookup Options above. As of router API 0.9.66.
```
Các triển khai khác nhau có thể không nhất quán trong việc trả về RESULT nào trong các tình huống khác nhau.

Hầu hết các phản hồi có RESULT, ngoại trừ OK, cũng sẽ bao gồm một MESSAGE với thông tin bổ sung. MESSAGE thường sẽ hữu ích trong việc gỡ lỗi các vấn đề. Tuy nhiên, các chuỗi MESSAGE phụ thuộc vào việc triển khai, có thể được hoặc không được dịch bởi máy chủ SAM sang ngôn ngữ hiện tại, có thể chứa thông tin nội bộ cụ thể của triển khai như các ngoại lệ, và có thể thay đổi mà không cần thông báo trước. Mặc dù các client SAM có thể chọn hiển thị các chuỗi MESSAGE cho người dùng, chúng không nên đưa ra các quyết định lập trình dựa trên những chuỗi đó, vì điều này sẽ dễ bị lỗi.

### Tùy chọn Tunnel, I2CP và Streaming

Các tùy chọn này có thể được truyền vào dưới dạng các cặp name=value trong dòng SAM SESSION CREATE.

Tất cả các phiên có thể bao gồm [các tùy chọn I2CP như độ dài và số lượng tunnel](/docs/protocol/i2cp#options). Các phiên STREAM có thể bao gồm [các tùy chọn thư viện Streaming](/docs/api/streaming#options).

Xem các tài liệu tham khảo đó để biết tên tùy chọn và giá trị mặc định. Tài liệu được tham chiếu dành cho phiên bản router triển khai bằng Java. Giá trị mặc định có thể thay đổi. Tên tùy chọn và giá trị có phân biệt chữ hoa chữ thường. Các phiên bản router khác có thể không hỗ trợ tất cả tùy chọn và có thể có giá trị mặc định khác; vui lòng tham khảo tài liệu router để biết chi tiết.

### Ghi chú BASE 64

Mã hóa Base 64 phải sử dụng bảng chữ cái Base 64 chuẩn của I2P "A-Z, a-z, 0-9, -, ~".

### Thiết lập SAM mặc định

Cổng SAM mặc định là 7656. SAM không được bật theo mặc định trong Java I2P Router; nó phải được khởi động thủ công, hoặc được cấu hình để tự động khởi động, trên trang cấu hình clients trong router console, hoặc trong tệp clients.config. Cổng SAM UDP mặc định là 7655, lắng nghe trên 127.0.0.1. Các cổng này có thể được thay đổi trong Java router bằng cách thêm các tham số sam.udp.port=nnnnn và/hoặc sam.udp.host=w.x.y.z vào lời gọi, hoặc trên dòng SESSION.

Cấu hình trong các router khác là tùy thuộc vào từng triển khai cụ thể. Xem [hướng dẫn cấu hình i2pd tại đây](https://i2pd.readthedocs.io/en/latest/user-guide/configuration/).
