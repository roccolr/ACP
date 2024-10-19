package implementazioni;
import interfacce.*;

public class CodaCircolare implements Coda{
    private int data[];
    private int size;
    private int elementi;
    private int head;
    private int tail;

    public CodaCircolare(int size){
        this.size = size;
        this.head = 0;
        this.tail = 0;
        this.elementi=0;
        this.data = new int[size];
    }

    public int getSize(){
        return this.size;
    }

    public boolean empty(){
        if(this.elementi == 0){
            return true;
        }
        else return false;
    }   

    public boolean full(){
        if(this.elementi == this.size){
            return true;
        }
        else return false;
    }

    //inseriamo in testa, preleviamo in coda
    //Questa coda è priva di metodi di sincronizzazione; useremo i blocchi sincronizzanti nei thread che fanno
    //operazioni su questa
    public void inserisci(int i){
        data[head] = i;
        elementi += 1;
        head = (head+1)%size;

        try{
            Thread.sleep(101+(int)(Math.random()*100));

        }catch(InterruptedException e){
            e.printStackTrace();
        }
               
        System.out.println("[INSERISCI] - inserito elemento: "+i+"; totale elementi: "+elementi+".");
    }

    public int preleva(){
        int result = data[tail];
        elementi -= 1;
        tail = (tail+1)%size;

        try{
            Thread.sleep(101+(int)Math.random()*100);
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        System.out.println("[PRELEVA]  prelevato elemento: "+result+"; totale elementi: "+elementi+".");
        return result;
    }
}
