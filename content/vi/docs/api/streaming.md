---
title: "Giao thức Streaming"
description: "Giao thức vận chuyển giống TCP được sử dụng bởi hầu hết các ứng dụng I2P"
slug: "streaming"
lastUpdated: "2025-07"
accurateFor: "0.9.67"
---

## Tổng quan {#overview}

Thư viện streaming về mặt kỹ thuật là một phần của tầng "ứng dụng", vì nó không phải là chức năng cốt lõi của router. Tuy nhiên, trong thực tế, nó cung cấp một chức năng quan trọng cho hầu hết tất cả các ứng dụng I2P hiện có, bằng cách cung cấp các luồng giống TCP qua I2P, và cho phép các ứng dụng hiện có được chuyển đổi dễ dàng sang I2P. Thư viện truyền tải end-to-end khác cho giao tiếp máy khách là [thư viện datagram](/docs/specs/datagrams).

Thư viện streaming là một lớp nằm trên [I2CP API](/docs/specs/i2cp) cốt lõi, cho phép các luồng tin nhắn đáng tin cậy, theo thứ tự và được xác thực hoạt động trên một lớp tin nhắn không đáng tin cậy, không theo thứ tự và không được xác thực. Giống như mối quan hệ giữa TCP và IP, chức năng streaming này có một loạt các đánh đổi và tối ưu hóa có sẵn, nhưng thay vì nhúng chức năng đó vào mã I2P cơ bản, nó đã được tách ra thành một thư viện riêng biệt để giữ cho các phức tạp giống TCP tách biệt và để cho phép các triển khai tối ưu hóa thay thế.

Xem xét chi phí tương đối cao của các thông điệp, giao thức của thư viện streaming cho việc lập lịch và gửi các thông điệp đó đã được tối ưu hóa để cho phép các thông điệp riêng lẻ được truyền chứa càng nhiều thông tin có sẵn càng tốt. Ví dụ, một giao dịch HTTP nhỏ được ủy quyền thông qua thư viện streaming có thể được hoàn thành trong một lần gửi-nhận duy nhất - các thông điệp đầu tiên gộp SYN, FIN và payload yêu cầu HTTP nhỏ, và phản hồi gộp SYN, FIN, ACK và payload phản hồi HTTP. Trong khi một ACK bổ sung phải được truyền để thông báo cho máy chủ HTTP rằng SYN/FIN/ACK đã được nhận, proxy HTTP cục bộ thường có thể gửi phản hồi đầy đủ đến trình duyệt ngay lập tức.

Thư viện streaming có nhiều điểm tương đồng với một sự trừu tượng hóa của TCP, với các cửa sổ trượt, thuật toán kiểm soát tắc nghẽn (cả slow start và congestion avoidance), và hành vi gói tin chung (ACK, SYN, FIN, RST, tính toán rto, v.v.).

Thư viện streaming là một thư viện mạnh mẽ được tối ưu hóa để hoạt động trên I2P. Nó có thiết lập một giai đoạn và chứa một triển khai windowing đầy đủ.

## API {#api}

API thư viện streaming cung cấp mô hình socket tiêu chuẩn cho các ứng dụng Java. API [I2CP](/docs/specs/i2cp) cấp thấp hơn được ẩn hoàn toàn, ngoại trừ việc các ứng dụng có thể truyền [tham số I2CP](/docs/specs/i2cp#options) thông qua thư viện streaming để được I2CP diễn giải.

Giao diện tiêu chuẩn cho thư viện streaming là ứng dụng sử dụng I2PSocketManagerFactory để tạo ra I2PSocketManager. Sau đó ứng dụng yêu cầu socket manager cung cấp một I2PSession, điều này sẽ tạo ra kết nối tới router thông qua [I2CP](/docs/specs/i2cp). Ứng dụng sau đó có thể thiết lập kết nối bằng I2PSocket hoặc nhận kết nối bằng I2PServerSocket.

Để xem ví dụ sử dụng tốt, hãy tham khảo mã nguồn i2psnark.

### Các tùy chọn và giá trị mặc định {#options}

Các tùy chọn và giá trị mặc định hiện tại được liệt kê dưới đây. Các tùy chọn phân biệt chữ hoa chữ thường và có thể được thiết lập cho toàn bộ router, cho một client cụ thể, hoặc cho một socket riêng lẻ trên cơ sở từng kết nối. Nhiều giá trị được điều chỉnh cho hiệu suất HTTP trong điều kiện I2P điển hình. Các ứng dụng khác như các dịch vụ peer-to-peer được khuyến khích mạnh mẽ sửa đổi khi cần thiết, bằng cách thiết lập các tùy chọn và truyền chúng qua cuộc gọi đến I2PSocketManagerFactory.createManager(_i2cpHost, _i2cpPort, opts). Giá trị thời gian tính bằng ms.

Lưu ý rằng các API tầng cao hơn, chẳng hạn như [SAM](/docs/api/samv3), [BOB](/docs/legacy/bob), và [I2PTunnel](/docs/api/i2ptunnel), có thể ghi đè các giá trị mặc định này bằng các giá trị mặc định riêng của chúng. Cũng lưu ý rằng nhiều tùy chọn chỉ áp dụng cho các server đang lắng nghe kết nối đến.

Kể từ phiên bản 0.9.1, hầu hết các tùy chọn, nhưng không phải tất cả, có thể được thay đổi trên socket manager hoặc session đang hoạt động. Xem javadocs để biết chi tiết.

<table style="width:100%; border-collapse:collapse; margin-bottom:1.5rem;">
  <thead>
    <tr>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Option</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Default</th>
      <th style="border:1px solid var(--color-border); padding:0.6rem; text-align:left; background:var(--color-bg-secondary);">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.accessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes used for either access list or blacklist. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.destination.sigType</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">DSA_SHA1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The name or number of the signature type for a transient destination. As of release 0.9.12.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableAccessList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a whitelist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2cp.enableBlackList</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Use the access list as a blacklist for incoming connections. As of release 0.7.13.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.answerPings</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to respond to incoming pings</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.blacklist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes to be blacklisted for incoming connections to ALL destinations in the context. This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.3.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.bufferSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">64K</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How much transmit data (in bytes) will be accepted that hasn't been written out yet.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.congestionAvoidanceGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in congestion avoidance, we grow the window size at the rate of <code>1/(windowSize*factor)</code>. In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to wait after instantiating a new con before actually attempting to connect. If this is &lt;= 0, connect immediately with no initial data. If greater than 0, wait until the output stream is flushed, the buffer fills, or that many milliseconds pass, and include any initial data with the SYN.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.connectTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">5*60*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on connect, in milliseconds. Negative means indefinitely. Default is 5 minutes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.disableRejectLogging</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">false</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to disable warnings in the logs when an incoming connection is rejected due to connection limits. As of release 0.9.4.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.dsalist</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">null</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Comma- or space-separated list of Base64 peer Hashes or host names to be contacted using an alternate DSA destination. Only applies if multisession is enabled and the primary session is non-DSA (generally for shared clients only). This option must be set in the context properties, NOT in the createManager() options argument. Note that setting this in the router context will not affect clients outside the router in a separate JVM and context. As of release 0.9.21.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.enforceProtocol</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">true</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Whether to listen only for the streaming protocol. Setting to true will prohibit communication with Destinations earlier than release 0.7.1 (released March 2009). Set to true if running multiple protocols on this Destination. As of release 0.9.1. Default true as of release 0.9.36.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">2 (send)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0=noop, 1=disconnect) What to do on an inactivity timeout - do nothing, disconnect, or send a duplicate ack.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.inactivityTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">90*1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Idle time before sending a keepalive</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialAckDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">750</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Delay before sending an ack</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialResendDelay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The initial value of the resend delay field in the packet header, times 1000. Not fully implemented; see below.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTO</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">9000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial timeout (if no <a href="#sharing">sharing data</a> available). As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialRTT</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8000</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Initial round trip time estimate (if no <a href="#sharing">sharing data</a> available). Disabled as of release 0.9.8; uses actual RTT.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.initialWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">6</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(if no <a href="#sharing">sharing data</a> available) In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.limitAction</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">reset</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">What action to take when an incoming connection exceeds limits. Valid values are: reset (reset the connection); drop (drop the connection); or http (send a hardcoded HTTP 429 response). Any other value is a custom response to be sent. backslash-r and backslash-n will be replaced with CR and LF. As of release 0.9.34.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConcurrentStreams</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(0 or negative value means unlimited) This is a total limit for incoming and outgoing combined.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(per peer; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxMessageSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1730</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">The maximum size of the payload, i.e. the MTU in bytes.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxResends</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">8</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Maximum number of retransmissions before failure.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerMinute</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Incoming connection limit (all peers; 0 means disabled). As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerHour</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxTotalConnsPerDay</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">(all peers; 0 means disabled) Use with caution as exceeding this will disable a server for a long time. As of release 0.7.14.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.maxWindowSize</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">128</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;"></td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.profile</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1 (bulk)</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1=bulk; 2=interactive; see important notes <a href="#profile">below</a>.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.readTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on read, in milliseconds. Negative means indefinitely.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.slowStartGrowthRateFactor</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">When we're in slow start, we grow the window size at the rate of 1/(factor). In standard TCP, window sizes are in bytes, while in I2P, window sizes are in messages. A higher number means slower growth.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.rttdevDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.tcbcache.wdwDampening</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">0.75</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">Ref: RFC 2140. Floating point value. May be set only via context properties, not connection options. As of release 0.9.8.</td>
    </tr>
    <tr>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">i2p.streaming.writeTimeout</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">-1</td>
      <td style="border:1px solid var(--color-border); padding:0.6rem;">How long to block on write/flush, in milliseconds. Negative means indefinitely.</td>
    </tr>
  </tbody>
</table>
## Đặc tả Giao thức {#spec}

[Xem trang Đặc tả Thư viện Streaming.](/docs/specs/streaming)

## Chi Tiết Triển Khai {#implementation}

### Thiết lập {#setup}

Bên khởi tạo gửi một gói tin với cờ SYNCHRONIZE được thiết lập. Gói tin này cũng có thể chứa dữ liệu ban đầu. Bên đồng cấp trả lời bằng một gói tin với cờ SYNCHRONIZE được thiết lập. Gói tin này cũng có thể chứa dữ liệu phản hồi ban đầu.

Bên khởi tạo có thể gửi thêm các gói dữ liệu, lên đến kích thước cửa sổ ban đầu, trước khi nhận được phản hồi SYNCHRONIZE. Những gói tin này cũng sẽ có trường send Stream ID được đặt thành 0. Bên nhận phải đệm các gói tin nhận được trên các stream chưa biết trong một khoảng thời gian ngắn, vì chúng có thể đến không theo thứ tự, trước gói tin SYNCHRONIZE.

### Lựa chọn và Thương lượng MTU {#mtu}

Kích thước thông điệp tối đa (còn gọi là MTU / MRU) được thương lượng theo giá trị thấp hơn được hỗ trợ bởi hai peer. Vì các thông điệp tunnel được đệm lên 1KB, việc chọn MTU kém sẽ dẫn đến một lượng lớn overhead. MTU được chỉ định bởi tùy chọn i2p.streaming.maxMessageSize. MTU mặc định hiện tại là 1730 được chọn để vừa chính xác vào hai thông điệp I2NP tunnel 1K, bao gồm overhead cho trường hợp điển hình.

Lưu ý: Đây là kích thước tối đa của payload (dữ liệu tải trọng) chỉ bao gồm phần dữ liệu, không bao gồm header.

Lưu ý: Đối với các kết nối ECIES, có overhead giảm, MTU được khuyến nghị là 1812. MTU mặc định vẫn là 1730 cho tất cả các kết nối, bất kể loại key nào được sử dụng. Client phải sử dụng giá trị nhỏ nhất của MTU được gửi và nhận, như thường lệ. Xem proposal 155.

Tin nhắn đầu tiên trong một kết nối bao gồm một Destination 387 byte (điển hình) được thêm bởi streaming layer, và thường là một LeaseSet 898 byte (điển hình), cùng với Session keys, được đóng gói trong tin nhắn Garlic bởi router. (LeaseSet và Session Keys sẽ không được đóng gói nếu một ElGamal Session đã được thiết lập trước đó). Do đó, mục tiêu đưa một HTTP request hoàn chỉnh vào một tin nhắn I2NP 1KB duy nhất không phải lúc nào cũng đạt được. Tuy nhiên, việc lựa chọn MTU, cùng với việc triển khai cẩn thận các chiến lược phân mảnh và gộp lô trong tunnel gateway processor, là những yếu tố quan trọng trong băng thông mạng, độ trễ, độ tin cậy và hiệu quả, đặc biệt đối với các kết nối tồn tại lâu dài.

### Tính toàn vẹn dữ liệu {#integrity}

Tính toàn vẹn dữ liệu được đảm bảo bởi checksum gzip CRC-32 được triển khai trong [lớp I2CP](/docs/specs/i2cp#format). Không có trường checksum trong giao thức streaming.

### Đóng gói Gói tin {#encapsulation}

Mỗi gói tin được gửi qua I2P dưới dạng một tin nhắn đơn lẻ (hoặc như một clove riêng lẻ trong [Garlic Message](/docs/overview/garlic-routing)). Việc đóng gói tin nhắn được thực hiện trong các lớp [I2CP](/docs/specs/i2cp), [I2NP](/docs/specs/i2np), và [tunnel message](/docs/specs/tunnel-message) bên dưới. Không có cơ chế phân định gói tin hoặc trường độ dài payload trong giao thức streaming.

### Độ trễ tùy chọn {#delay}

Các gói dữ liệu có thể bao gồm một trường delay tùy chọn chỉ định độ trễ được yêu cầu, tính bằng ms, trước khi bên nhận phải ack gói tin. Các giá trị hợp lệ là từ 0 đến 60000 (bao gồm). Giá trị 0 yêu cầu ack ngay lập tức. Đây chỉ là khuyến nghị, và các bên nhận nên trễ một chút để có thể ack nhiều gói tin khác bằng một ack duy nhất. Một số triển khai có thể bao gồm giá trị khuyến nghị (RTT đo được / 2) trong trường này. Đối với các giá trị delay tùy chọn khác không, các bên nhận nên giới hạn độ trễ tối đa trước khi gửi ack tối đa vài giây. Các giá trị delay tùy chọn lớn hơn 60000 chỉ ra tình trạng nghẹt, xem bên dưới.

### Cửa sổ Truyền/Nhận và Chặn {#windows}

Các header TCP bao gồm cửa sổ nhận theo byte; tuy nhiên, giao thức streaming không cung cấp cách thức để trao đổi kích thước cửa sổ nhận tối đa theo byte hoặc gói tin. Chỉ có một chỉ báo choke/unchoke đơn giản cho biết rằng bộ đệm nhận đã đầy. Mỗi điểm cuối phải duy trì ước tính riêng về cửa sổ nhận của đầu xa, theo byte hoặc gói tin. Lưu ý rằng bộ đệm nhận có thể bị tràn ở bất kỳ kích thước cửa sổ nào nếu ứng dụng client chậm trong việc làm trống bộ đệm.

Kích thước cửa sổ truyền và nhận tối đa mặc định trong triển khai Java là 128 gói tin. Các triển khai thiết lập kích thước cửa sổ truyền tối đa cao hơn 128 phải xem xét các vấn đề sau:

- Các phản hồi CHOKE từ Java router do tràn bộ đệm nhận có khả năng xảy ra cao hơn nhiều.
- Việc ước tính kích thước bộ đệm nhận ở đầu xa phải được triển khai để giảm thiểu tình trạng tràn lặp lại (xem phía trên)
- CHOKE phải được xử lý một cách chính xác (xem phía dưới)
- Kích thước cửa sổ tối đa trên 256 thậm chí còn dễ xảy ra lỗi hơn, vì độ dài trường tùy chọn đếm nack là một byte, giới hạn số NACK tối đa là 255. Đặc tả này không đề cập đến việc phải làm gì nếu có hơn 255 NACK. Kích thước cửa sổ tối đa trên 256 không được khuyến nghị.

Kích thước buffer tối thiểu được khuyến nghị cho các triển khai receiver là 128 packet hoặc 232 KB (xấp xỉ 128 * 1812). Do độ trễ mạng I2P, packet bị mất, và việc kiểm soát tắc nghẽn kết quả, buffer có kích thước này hiếm khi bị đầy. Tuy nhiên, tình trạng tràn buffer có khả năng xảy ra cao hơn nhiều trên các kết nối băng thông rộng "local loopback" (cùng router) hoặc trong quá trình thử nghiệm cục bộ.

Để nhanh chóng báo hiệu và phục hồi mượt mà từ các tình trạng tràn bộ đệm, có một cơ chế đơn giản cho pushback trong giao thức streaming. Nếu một gói tin được nhận với trường delay tùy chọn có giá trị 60001 hoặc cao hơn, điều đó cho biết trạng thái "choking" hoặc cửa sổ nhận bằng không. Một gói tin với trường delay tùy chọn có giá trị 60000 hoặc thấp hơn cho biết trạng thái "unchoking". Các gói tin không có trường delay tùy chọn không ảnh hưởng đến trạng thái choke/unchoke.

Sau khi bị chặn (choked), không nên gửi thêm gói tin nào có dữ liệu cho đến khi thiết bị truyền được bỏ chặn (unchoked), ngoại trừ các gói tin dữ liệu "thăm dò" (probe) thỉnh thoảng để bù đắp cho các gói tin bỏ chặn có thể bị mất. Điểm cuối bị chặn nên khởi động "bộ đếm thời gian kiên trì" để kiểm soát việc thăm dò, như trong TCP. Điểm cuối bỏ chặn nên gửi một số gói tin với trường này được đặt, hoặc tiếp tục gửi chúng định kỳ cho đến khi nhận được gói tin dữ liệu trở lại. Thời gian tối đa để chờ bỏ chặn phụ thuộc vào cách triển khai. Kích thước cửa sổ truyền và chiến lược kiểm soát tắc nghẽn sau khi được bỏ chặn phụ thuộc vào cách triển khai.

### Kiểm Soát Tắc Nghẽn {#congestion}

Thư viện streaming sử dụng các pha slow-start tiêu chuẩn (tăng trưởng cửa sổ theo cấp số nhân) và tránh tắc nghẽn (tăng trưởng cửa sổ tuyến tính), với exponential backoff. Windowing và acknowledgments sử dụng số lượng gói tin, không phải số lượng byte.

### Đóng {#close}

Bất kỳ gói tin nào, bao gồm cả gói tin có thiết lập cờ SYNCHRONIZE, cũng có thể được gửi kèm với cờ CLOSE. Kết nối sẽ không được đóng cho đến khi peer phản hồi với cờ CLOSE. Các gói tin CLOSE cũng có thể chứa dữ liệu.

### Ping / Pong {#ping}

Không có chức năng ping ở lớp I2CP (tương đương với ICMP echo) hay trong datagram. Chức năng này được cung cấp trong streaming. Ping và pong không thể kết hợp với gói streaming tiêu chuẩn; nếu tùy chọn ECHO được thiết lập, thì hầu hết các cờ, tùy chọn, ackThrough, sequenceNum, NACK khác sẽ bị bỏ qua.

Một gói ping phải có các cờ ECHO, SIGNATURE_INCLUDED, và FROM_INCLUDED được thiết lập. sendStreamId phải lớn hơn không, và receiveStreamId bị bỏ qua. sendStreamId có thể tương ứng hoặc không tương ứng với một kết nối hiện có.

Một gói pong phải có cờ ECHO được thiết lập. Giá trị sendStreamId phải bằng không, và receiveStreamId chính là sendStreamId từ gói ping. Trước phiên bản 0.9.18, gói pong không bao gồm bất kỳ payload nào có trong gói ping.

Từ phiên bản 0.9.18, các ping và pong có thể chứa payload. Payload trong ping, tối đa 32 byte, sẽ được trả về trong pong.

Streaming có thể được cấu hình để vô hiệu hóa việc gửi pong bằng cách đặt i2p.streaming.answerPings=false.

### Ghi chú về i2p.streaming.profile {#profile}

Tùy chọn này hỗ trợ hai giá trị; 1=bulk và 2=interactive. Tùy chọn này cung cấp gợi ý cho thư viện streaming và/hoặc router về mẫu lưu lượng dự kiến.

"Bulk" có nghĩa là tối ưu hóa cho băng thông cao, có thể phải đánh đổi độ trễ. Đây là cài đặt mặc định. "Interactive" có nghĩa là tối ưu hóa cho độ trễ thấp, có thể phải đánh đổi băng thông hoặc hiệu suất. Các chiến lược tối ưu hóa, nếu có, phụ thuộc vào cách triển khai và có thể bao gồm những thay đổi bên ngoài giao thức streaming.

Từ phiên bản API 0.9.63, Java I2P sẽ trả về lỗi cho bất kỳ giá trị nào khác ngoài 1 (bulk) và tunnel sẽ không khởi động được. Từ API 0.9.64, Java I2P bỏ qua giá trị này. Từ phiên bản API 0.9.63, i2pd đã bỏ qua tùy chọn này; nó được triển khai trong i2pd từ API 0.9.64.

Mặc dù giao thức streaming bao gồm một trường flag để truyền cài đặt profile tới đầu kia, điều này không được triển khai trong bất kỳ router nào đã biết.

### Chia sẻ Control Block {#sharing}

Streaming lib hỗ trợ chia sẻ "TCP" Control Block. Điều này chia sẻ ba tham số quan trọng của streaming lib (kích thước cửa sổ, thời gian khứ hồi, phương sai thời gian khứ hồi) qua các kết nối đến cùng một peer từ xa. Điều này được sử dụng cho chia sẻ "tạm thời" tại thời điểm mở/đóng kết nối, không phải chia sẻ "tập hợp" trong suốt một kết nối (Xem [RFC 2140](http://www.ietf.org/rfc/rfc2140.txt)). Có một chia sẻ riêng biệt cho mỗi ConnectionManager (tức là mỗi Destination cục bộ) để không có rò rỉ thông tin đến các Destination khác trên cùng một router. Dữ liệu chia sẻ cho một peer nhất định sẽ hết hạn sau vài phút. Các tham số Control Block Sharing sau có thể được thiết lập cho mỗi router:

- RTT_DAMPENING = 0.75
- RTTDEV_DAMPENING = 0.75
- WINDOW_DAMPENING = 0.75

### Các Tham Số Khác {#other}

Các tham số sau đây là giá trị mặc định được khuyến nghị. Giá trị mặc định có thể khác nhau, tùy thuộc vào cách triển khai:

- MIN_RESEND_DELAY = 100 ms (RTO tối thiểu)
- MAX_RESEND_DELAY = 45 giây (RTO tối đa)
- MIN_WINDOW_SIZE = 1
- MAX_WINDOW_SIZE = 128
- TREND_COUNT = 3
- MIN_MESSAGE_SIZE = 512 (MTU tối thiểu)
- INBOUND_BUFFER_SIZE = maxMessageSize * (maxWindowSize + 2)
- INITIAL_TIMEOUT (chỉ có hiệu lực trước khi RTT được lấy mẫu) = 9 giây
- "alpha" (hệ số giảm chấn RTT theo RFC 6298) = 0.125
- "beta" (hệ số giảm chấn RTTDEV theo RFC 6298) = 0.25
- "K" (hệ số nhân RTDEV theo RFC 6298) = 4
- PASSIVE_FLUSH_DELAY = 175 ms
- Ước tính RTT tối đa: 60 giây

### Lịch sử {#history}

Thư viện streaming đã phát triển một cách tự nhiên cho I2P - đầu tiên mihi đã triển khai "mini streaming library" như một phần của I2PTunnel, với giới hạn window size chỉ 1 tin nhắn (yêu cầu ACK trước khi gửi tin nhắn tiếp theo), sau đó nó được tái cấu trúc thành một giao diện streaming tổng quát (phản chiếu TCP socket) và việc triển khai streaming đầy đủ được triển khai với giao thức sliding window và các tối ưu hóa để tính đến tích số bandwidth x delay cao. Các stream riêng lẻ có thể điều chỉnh kích thước packet tối đa và các tùy chọn khác. Kích thước tin nhắn mặc định được chọn để khớp chính xác với hai I2NP tunnel message 1K, và là sự cân bằng hợp lý giữa chi phí bandwidth của việc truyền lại các tin nhắn bị mất, và độ trễ cũng như overhead của nhiều tin nhắn.

## Công việc tương lai {#future}

Hành vi của thư viện streaming có tác động sâu sắc đến hiệu suất ở tầng ứng dụng, và do đó, đây là một lĩnh vực quan trọng cần phân tích thêm.

- Có thể cần thiết điều chỉnh thêm các tham số của streaming lib.
- Một lĩnh vực nghiên cứu khác là sự tương tác của streaming lib với các lớp transport NTCP và SSU. Xem [trang thảo luận NTCP](/docs/historical/ntcp-discussion) để biết chi tiết.
- Sự tương tác của các thuật toán định tuyến với streaming lib ảnh hưởng mạnh đến hiệu suất. Cụ thể, việc phân phối ngẫu nhiên các tin nhắn đến nhiều tunnel trong một pool dẫn đến mức độ cao việc giao hàng không theo thứ tự, kết quả là kích thước cửa sổ nhỏ hơn so với trường hợp bình thường. Router hiện tại định tuyến các tin nhắn cho một cặp đích từ/đến duy nhất thông qua một tập hợp tunnel nhất quán, cho đến khi tunnel hết hạn hoặc giao hàng thất bại. Các thuật toán lỗi và lựa chọn tunnel của router nên được xem xét để có thể cải thiện.
- Dữ liệu trong gói SYN đầu tiên có thể vượt quá MTU của người nhận.
- Trường DELAY_REQUESTED có thể được sử dụng nhiều hơn.
- Các gói SYNCHRONIZE ban đầu trùng lặp trên các luồng tồn tại ngắn có thể không được nhận dạng và loại bỏ.
- Không gửi MTU trong việc truyền lại.
- Dữ liệu được gửi đi trừ khi cửa sổ outbound đầy. (tức là no-Nagle hoặc TCP_NODELAY) Có lẽ nên có một tùy chọn cấu hình cho điều này.
- zzz đã thêm mã debug vào thư viện streaming để ghi log các gói theo định dạng tương thích với wireshark (pcap); Sử dụng điều này để phân tích thêm hiệu suất. Định dạng có thể cần cải tiến để ánh xạ nhiều tham số streaming lib hơn vào các trường TCP.
- Có những đề xuất thay thế streaming lib bằng TCP tiêu chuẩn (hoặc có thể là một lớp null cùng với raw socket). Điều này thật không may sẽ không tương thích với streaming lib nhưng sẽ tốt nếu so sánh hiệu suất của hai cái.
