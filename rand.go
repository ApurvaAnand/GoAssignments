package main
import "fmt"
import "os"
import "math"
import "math/rand"
import "strconv"

func randTheta() float64{

	return (rand.Float64() )
}


func randomwalk(w int,h float64,d float64,n float64){
	var c = float64(w)

	var a,b = c/2,h/2

	var x,y float64
	x=float64(a)
	y=float64(b)

	for i := 0.0; i < n; i++ {
		var dx, dy float64


		dx = d*math.Cos(randTheta()*2*math.Pi)
		for x+dx < 0 || x+dx >= c{ 

			dx = d*math.Cos(randTheta()*2*math.Pi)
		} 
		x=x+dx

		dy = d*math.Sin(randTheta()*2*math.Pi)
		for y+dy < 0 || y+dy >= h {
			dy = d*math.Sin(randTheta()*2*math.Pi)
		} 
		y=y+dy



		fmt.Println(x,y)
	}


	var distance float64 = (math.Sqrt(math.Pow((x-c),2)+math.Pow((y-h),2)))
	fmt.Println("distance=",distance)

}


func main() {


	var w,_=strconv.Atoi(os.Args[1])

	var h,_=strconv.ParseFloat((os.Args[2]),64)
	var d,_=strconv.ParseFloat((os.Args[3]),64)
	var n,_=strconv.ParseFloat((os.Args[4]),64)
	var s,_=strconv.ParseInt((os.Args[5]),10,64)
	if (w <= 0 || h <= 0 || d <=0 || n <=0 || s <= 0) {
		fmt.Println("error:argument is zero or negative")
		os.Exit(0)
	}
	// fmt.Println(h)
	rand.Seed(s)

	randomwalk(w,h,d,n)

}




