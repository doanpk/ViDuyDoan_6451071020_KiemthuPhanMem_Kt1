# TEST CASE – TRANG ĐĂNG NHẬP TÀI KHOẢN VĂN PHÒNG ĐIỆN TỬ
**Hệ thống:** Tài khoản văn phòng điện tử – Trường ĐH Giao Thông Vận Tải (UTC)  
**URL:** vanphongdientu.utc.edu.vn  
**Người viết:** QA Team  
**Ngày viết:** 08/10/2026  

---

| STT | ID  | Description | Steps | Expected Output |
|-----|-----|-------------|-------|-----------------|
| 1 | TC1 | Để trống user hoặc pass word | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô pass<br>3. Nhập pass là "1256"<br>4. Click vào nút Login | Bạn chưa nhập tên đăng nhập |
| 2 | TC2 | Để trống mật khẩu | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập ô username<br>3. Nhập user là huongngt<br>4. Click vào nút Login | Bạn chưa nhập mật khẩu |
| 3 | TC3 | Đúng tên sai mật khẩu | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô username<br>3. Nhập user là huongngt<br>4. Click vào ô pass<br>5. Nhập pass là: utc@235<br>6. Click vào nút Login | Tài khoản không đúng |
| 4 | TC4 | Sai tên, đúng mật khẩu | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô username<br>3. Nhập user là lihuongthunguyen<br>4. Click vào ô pass<br>5. Nhập pass là: 123456@utc<br>6. Click vào nút Login | Tài khoản không đúng |
| 5 | TC5 | Đăng nhập thành công và chọn "Giữ tôi luôn đăng nhập" | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô username<br>3. Nhập user là huongngt<br>4. Click vào ô pass<br>5. Nhập pass là: 123456@utc<br>6. Tích chọn "Giữ tôi luôn đăng nhập"<br>7. Click vào nút Login<br>8. Tắt trình duyệt và mở lại | Đưa vào trang chủ.<br><br>Vào trang chủ |
| 6 | TC6 | Đăng nhập thành công và không chọn "Giữ tôi luôn đăng nhập" | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô username<br>3. Nhập user là huongngt<br>4. Click vào ô pass<br>5. Nhập pass là: 123456@utc<br>6. Click vào nút Login<br>7. Tắt trình duyệt và mở lại | Đưa vào trang chủ.<br><br>Vào trang đăng nhập |
| 7 | TC7 | Đăng nhập bằng e-mail UTC | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào nút "Đăng nhập bằng e-mail UTC" | Chuyển hướng đến trang xác thực email UTC (@utc.edu.vn) |
| 8 | TC8 | Quên mật khẩu | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào link "Bạn quên mật khẩu đăng nhập ?" | Chuyển đến trang khôi phục mật khẩu |
| 9 | TC9 | SQL Injection vào trường đăng nhập | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập vào ô username: ' OR '1'='1<br>3. Nhập bất kỳ mật khẩu<br>4. Click vào nút Login | Tài khoản không đúng, không cho phép đăng nhập |
| 10 | TC10 | Mật khẩu hiển thị dạng ẩn | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô pass<br>3. Nhập ký tự bất kỳ | Mật khẩu hiển thị dạng ký tự ẩn (●●●●), không lộ mật khẩu rõ |
| 11 | TC11 | Mật khẩu phân biệt chữ hoa/thường | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào ô username<br>3. Nhập user là huongngt<br>4. Click vào ô pass<br>5. Nhập pass là: 123456@UTC (sai hoa/thường)<br>6. Click vào nút Login | Tài khoản không đúng |
| 12 | TC12 | Đăng nhập sai nhiều lần liên tiếp | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Nhập user là huongngt<br>3. Nhập pass sai liên tục 5 lần<br>4. Click vào nút Login sau mỗi lần | Hệ thống hiển thị CAPTCHA hoặc khóa tài khoản tạm thời |
| 13 | TC13 | Giao diện hiển thị đúng trên mobile | 1. Mở trang vanphongdientu.utc.edu.vn trên điện thoại (hoặc DevTools 375px)<br>2. Quan sát bố cục trang | Các thành phần hiển thị đầy đủ, không bị cắt xén, dễ thao tác |
| 14 | TC14 | Link "Trung tâm trợ giúp" hoạt động | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào link "Trung tâm trợ giúp" ở footer | Chuyển đến trang trung tâm trợ giúp, không bị lỗi 404 |
| 15 | TC15 | Link "Ý kiến phản hồi" hoạt động | 1. Mở trang vanphongdientu.utc.edu.vn<br>2. Click vào link "Ý kiến phản hồi" ở footer | Chuyển đến trang gửi ý kiến phản hồi, không bị lỗi 404 |
