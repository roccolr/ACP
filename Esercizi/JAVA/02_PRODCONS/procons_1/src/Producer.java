public class Producer extends Thread{
    private Buffer b;
    
    public Producer(Buffer b, String name){
        super(name);
        this.b=b;
    }

    public void run(){
        b.produci();
    }
}
