public class Buffer {
    private long content;
    private boolean full;

    public Buffer(){
        content = 0;
        full = false;
    }

    public synchronized void produci(){
        System.out.println(Thread.currentThread().getName() + "\tinvoca produci");

        while(full){
            try{
                wait();
            }
            catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        
        content = System.currentTimeMillis();

        System.out.println(Thread.currentThread().getName()+"\tprodotto: " + content);
        full = true;        
        notifyAll();
    }

    public synchronized void consuma(){
        System.out.println(Thread.currentThread().getName()+"\tinvoca consuma");

        while(!full){
            try{
                wait();
            }
            catch (InterruptedException e){
                e.printStackTrace();
            }
        }

        System.out.println(Thread.currentThread().getName()+"\tconsumo: "+content);

        full = false;

        notifyAll();;
    }
}
