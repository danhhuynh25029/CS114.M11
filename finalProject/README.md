<h1 align="center">
Đồ án cuối kì môn máy học - CS114.M11
</h1>
<h1 align="center">
    Phát hiện một số bệnh trên lá cây cà phê
</h1>

## Bảng mục lục
1.[Giới thiệu bài toán](#giới-thiệu-bài-toán)

2.[Bộ dữ liệu](#xây-dựng-bộ-dữ-liệu)

3.[Mô hình sử dụng](#)

4.[Phương pháp đánh giá](#)

5.[Đánh giá kết quả](#)

6.[Hướng phát triển](#)

7.[Tài liệu tham khả0](#Tài-liệu-tham-khảo)
<hr>

## 1.Giới thiệu bài toán:

* Ngữ cảnh ứng dụng : 
    
    * Cà phê là một thức uống được sử dụng phổ biến hiện nay và lượng tiêu thụ cà phê trên thế giới rất cao.Vì vậy ngày càng nhiều vườn trồng cà phê ra đời nhằm phục vụ cho sản lượng tiêu thụ lớn.Cà phê cũng giống như các loại cây nông nghiệp khác đều có thể mắc chứng bệnh trên lá cây gây ảnh hưởng đến sức khỏe của cây và ảnh hưởng đến năng suất trồng trọt.Nhận thấy được vấn đề đó nên nhóm đã quyết định áp dụng những kiến thức của mình và những công nghệ có sẵn hiện nay để giải quyết bài toán phát hiện bệnh trên lá cây cà phê
    * Vậy tại sao lại cần giải quyết bài toán này.Các vườn trồng cà phê ngày một gia tăng thì cũng với đó nếu những người nông nhân đã có kinh nghiệm trồng cà phê lâu năm thì có thể dễ dàng xác định xem bệnh trên lá cây đó là bệnh gì.Tuy nhiên nếu người mới bước vào nghề chưa biết gì về cà phê thì sẽ cần đến một ứng dụng có thể giúp người mới trồng phát hiện bệnh và có cách xử lý phù hợp.
* Input và Output:
    
    * Input:
        
        * Một tấm ảnh chụp bằng camera điện thoại thông minh
        * Điều kiện :
            * Ban ngày
            * Không bị chói nắng
            * Chụp mặt trên của lá cây cà phê
    * Output:

        * Bounding box bao quanh các vị trí bệnh trên lá cây
        * Tên loại bệnh

## 2.Bộ dữ liệu:

* ### Quá trình thu thập:
    * Dữ liệu được nhóm thu thập thủ công bằng điện thoại.Thu thập thủ công tại vườn giúp bộ dữ liệu gần sát với thực tế khi người nông dân tiến hành chụp.
* ### Tiêu chí khi thu thập dữ liệu :
    * Chụp toàn bộ chiếc lá
    * Đảm bộ độ sáng phù hợp
    * khoảng cách chụp vừa phải
    * Gốc camera từ trên xuống
* ### Nơi thu thập dữ liệu :
    * Vườn cà phê của nhà người thân xa khoảng 40km
* ### Khó khắn khi thu thập dữ liệu : 
    * Đường đi xa xôi.Hiện nay dịch bệnh vẫn còn ảnh hưởng nên có rất nhiều khó khăn trong việc đi lại và có thể gây ảnh hưởng đến sức khỏe
* ### Tổng quan về bộ dữ liệu :
    * Bộ dữ liệu gồm có 3827 tấm ảnh thuộc bốn lớp là bốn loại bệnh phổ biến xuất hiện trên lá cây cà phê
    * Bốn loại bệnh : 
        * Sâu vẽ bùa
        * Phấn trắng
        * Nấm rỉ sắt
        * Đốm rong 
* ### Thống số bộ dữ liệu : 
    * Tập dữ liệu sẽ được chia thành hai tập train và test với tỉ lệ là 8:2
    
    Cần một tấm hình
## 3.Mô hình sử dụng:
* Yolov4:
    * Giới thiệu:
* Yolov5:
    * Giới thiệu:
* Faster-RCNN:
    * Giới thiệu:
## 4.Phương pháp đánh giá

