abstract class Shape {
    abstract double calculateArea();
}

class Circle extends Shape {
    double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double calculateArea() {
        return Math.PI * radius * radius;
    }
}

class Rectangle extends Shape {
    double length;
    double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    double calculateArea() {
        return length * width;
    }
}

public class Main {
    public static void main(String[] args) {
        Circle myCircle = new Circle(3.5);
        double circleArea = myCircle.calculateArea();
        System.out.println("Circle area: " + circleArea);

        Rectangle myRectangle = new Rectangle(4.0, 6.0);
        double rectangleArea = myRectangle.calculateArea();
        System.out.println("Rectangle area: " + rectangleArea);
    }
}
