# *<p style="text-align: center;">ỨNG DỤNG CỦA LINEAR REGRESSION TRONG VIỆC DỰ ĐOÁN GIÁ THUÊ TRỌ</p>*
## *1. Lý do chọn đề tài*
<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Khi bước vào ngưỡng cửa đại học với bao ước mơ, hoài bão của tuổi thanh xuân, công việc đầu tiên của các
            sinh viên chính là tìm một phòng trọ để thuê trong những năm học đại học. Những sinh viên lần đầu tiên bước
            chân vào đất Sài Thành có lẽ sẽ khá bỡ ngỡ trong thời gian đầu, có thể chưa quen về giá cả, lối sống,... của
            người dân nơi đây. Vì lẽ đó, những việc "chặt chém" giá những căn phòng cho thuê đã không còn là những điều
            xa lạ.</p>
        <p style="text-align: justify;">
            Nhóm chúng tôi vô cùng thấu hiểu và đồng cảm với những người đã bị chủ trọ, chủ nhà đưa ra một cái giá đắt
            hơn nhiều so với mặt bằng chung mà vẫn nhẹ dạ cả tin chi một số tiền không hề nhỏ trong phần kinh phí vốn eo
            hẹp của mình. Thế nên chúng tôi quyết định xây dựng một phần mềm dự đoán giá thuê trọ trong khu vực Thành
            phố Hồ Chí Minh, nơi chúng tôi học tập và sinh sống, đồng thời cũng là nơi thực hiện khảo sát và thu thập dữ
            liệu để huấn luyện model của mình.</p>
    </div>
</div>

## *2. Sản phẩm*
### *2.1 Giao diện chính*
<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Nhằm thuận tiện trong việc tiếp cận với nhiều đối tượng, chúng tôi đã xây dựng một giao diện đơn giản và
            thân thiện với người dùng như sau:</p>
    </div>
</div>

<p style="text-align: center"><img
        src="https://scontent.fsgn5-2.fna.fbcdn.net/v/t1.15752-9/386856336_331112466341856_5127594010464059834_n.png?_nc_cat=105&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=c-4bDwjSSNgAX_29llw&_nc_ht=scontent.fsgn5-2.fna&oh=03_AdTsTNc73xrEjPshScnH063kuvWfgyvxC9yceu9PvPy44w&oe=6597446D">
</p>

<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Đầu tiên, để dự đoán giá của một phòng trọ, chúng tôi đưa ra các tiêu chí như sau: diện tích sàn được tính
            theo mét vuông, số phòng ngủ có các lựa chọn là: 1, 2 và 3, số phòng tắm cũng có các lựa chọn là: 1, 2 hay 3
            phòng, nội thất được chia thành ba mức độ: không có, cơ bản (có giường, tủ) và đầy đủ (có giường, tủ, bàn
            ghế, có dán tường và trang trí,...). Ngoài ra các tiện nghi đi kèm được thể hiện bằng các ô, khi người dùng
            muốn sử dụng máy giặt (chung hoặc riêng để đỡ phải giặt tay), nhà bếp, điều hòa, bãi giữ xe hay có ban công
            thì có thể bấm chọn vào các ô bên cạnh tiện nghi mong muốn.</p>
    </div>
</div>
<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Để minh họa việc sử dụng nhóm chúng tôi đưa ra một ví dụ cụ thể như sau: Bạn A đang tìm một căn phòng rộng
            15 mét vuông, 1 phòng ngủ, 1 phòng tắm, có máy giặt, điều hòa và bãi giữ xe, khoảng cách tới trung tâm thành
            phố khoảng 2km. Phần mềm sẽ đưa ra dự đoán giá phòng vào khoảng 3,146,157 Đồng một tháng.</p>
    </div>
</div>
<p style="text-align: center"><img
        src="https://scontent.fsgn2-8.fna.fbcdn.net/v/t1.15752-9/386858651_1017524529678203_1311701599767552252_n.png?_nc_cat=102&ccb=1-7&_nc_sid=8cd0a2&_nc_ohc=51xIQ27OSd4AX8wSc8h&_nc_ht=scontent.fsgn2-8.fna&oh=03_AdRhu9E-SNyJEw9j58DSZYdGQkb1agXK19sXg5Ouzlll7w&oe=65974875">
</p>

### *2.2 Thuật toán đã sử dụng*
<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Trong phần mềm, chúng tôi đã gọi trực tiếp hàm Linear Regression từ thư viện sklearn nên chúng tôi sẽ trình
            bày sơ lược về Hàm mất mát (Loss Function), đây là một hàm vô cùng quan trọng trong Linear Regression nói
            riêng và Machine Learning nói chung.
        </p>
    </div>
</div>

<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Loss function là một phương pháp đo lường chất lượng của mô hình dự đoán trên tập dữ liệu quan sát. Nếu mô
            hình dự đoán sai nhiều thì giá trị của loss function sẽ càng lớn và ngược lại nếu nó dự đoán càng đúng thì
            giá trị của Loss Function sẽ càng nhỏ. Ta có công thức chung cho hàm mất mát như sau:</p>
    </div>
</div>

$$L(\hat{y},y) = \frac{1}{2}(\hat{y}-y)^2$$

<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Chúng ta có thể tính được giá trị mất mát do mô hình dự đoán tại tất cả các điểm trong bộ dữ liệu quan sát.
            Giá trị này có thể lớn, có thể nhỏ và khá rời rạc nên chúng ta không thể biết được đâu là dự đoán tốt, đâu
            là dự đoán không tốt, vì vậy để đánh giá mức độ tốt của mô hình dự đoán, chúng ta lấy trung bình giá trị mất
            mát của toàn bộ các điểm trên bộ dữ liệu quan sát. Điều này giúp ta xác định được một Loss Function trên
            toàn bộ bộ dữ liệu quan sát:</p>
    </div>
</div>


![img alt="text"](https://sebastianraschka.com/images/faq/closed-form-vs-gd/simple_regression.png)

<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Loss function là các hàm đo lường mức độ dự đoán sai của mô hình trên dữ liệu quan sát hữu hạn, nó là trung
            bình lỗi dự đoán trên toàn bộ bộ dữ liệu. Ngoài ra nó còn có đạo hàm dễ xác định để tiện cho việc tối ưu hóa
            sử dụng các thuật toán dựa trên đạo hàm hay Gradient Descent. Tuy nhiên, trong thực tế Linear Regression
            được cài đặt bằng cách tính đạo hàm tìm nghiệm trực tiếp vì lý do hiệu năng nên chúng tôi sẽ không giới
            thiệu ở đây.</p>
    </div>
</div>

## *3. Kết luận*
<div style="display: flex; gap: 2rem;">
    <div>
        <p style="text-align: justify;">
            Bằng việc tìm tòi và sử dụng các kĩ thuật trong Machine Learning, cụ thể là Linear Regression, chúng tôi đã
            có một cái nhìn tổng quát hơn trong việc tạo lập các model Trí Tuệ Nhân Tạo, đây là một bước đệm vô cùng
            quan trọng cho sự phát triển của ứng dụng dự đoán giá thuê nhà và đồng thời cũng là các model khác trong
            tương lai.</p>
        <p style="text-align: justify;">
            Tựu trung, với mong muốn phần nào giúp đỡ được phần nào các bạn tân sinh viên chập chững những bước đầu trên
            con đường học vấn của mình. Chúng tôi mong muốn phần mềm có thể được phát triển hơn, cung cấp giá dự đoán
            chính xác hơn để có thể tiếp cận và giúp đỡ thêm nhiều sinh viên cũng như các đối tượng khác có nhu cầu thuê
            nhà muốn tham khảo giá thị trường chung.</p>