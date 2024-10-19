package client;

import java.util.Hashtable;

import javax.jms.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import java.util.Random;
/*
 * * ``"java.naming.factory.initial" -> "org.apache.activemq.jndi.ActiveMQInitialContextFactory"``
* ``"java.naming.provider.url" -> "tcp://127.0.0.1:61616"``
 * 
 * 
 * 
 */




public class Client {
    public static void main(String argv[]){

        final int numero_richiesta = 20;

        Hashtable <String, String> prop = new Hashtable<>();
        prop.put("java.naming.factory.initial", "org.apache.activemq.jndi.ActiveMQInitialContextFactory");
        prop.put("java.naming.provider.url", "tcp://127.0.0.1:61616");
        prop.put("topic.request", "request_topic");

        try{
            String tipoRichiesta = argv[0];
            System.out.println("Client avviato per generare richieste di tipo "+tipoRichiesta);
            Context jndiContext = new InitialContext(prop);
            Random random = new Random();
            //ottengo gli administered objects 
            TopicConnectionFactory topicConnectionFactory = (TopicConnectionFactory)jndiContext.lookup("TopicConnectionFactory");
            Topic requestTopic = (Topic)jndiContext.lookup("request");

            //ottengo la connection
            TopicConnection conn = topicConnectionFactory.createTopicConnection();
            
            //ottengo la sessione
            TopicSession session = conn.createTopicSession(false, Session.AUTO_ACKNOWLEDGE);

            TopicPublisher publisher = session.createPublisher(requestTopic);

            MapMessage msg = session.createMapMessage();
            // AB000CD

            for(int i=0; i<numero_richiesta; i++){
                msg.setString("tipo", tipoRichiesta);
                
                if(tipoRichiesta.equalsIgnoreCase("compra")){
                    String targa = "AB"+random.nextInt(9)+random.nextInt(9)+random.nextInt(9)+"CD";
                    msg.setString("valore", targa+"-"+(random.nextInt(1000)+8999));
                }else if(tipoRichiesta.equalsIgnoreCase("vendi")){
                    String cliente = "giggino"+"-"+(random.nextInt(1000)+8999);
                    msg.setString("valore", cliente);
                }else{
                    System.out.println("[CLIENT]\tRichiesta non riconosciuta");
                    break;
                }

                publisher.send(msg);
                System.out.println("[CLIENT]\tinviato messaggio: "+msg.getString("tipo") + ": "+msg.getString("valore")); 
            }

            System.out.println("[CLIENT]\tFine invio");

            // String targa = (new String(first))+(random.nextInt(9))+(random.nextInt(9))+(random.nextInt(9))+(new String(second));

            conn.close();

        }catch(NamingException e){
            e.printStackTrace();;
        }catch(JMSException e){
            e.printStackTrace();
        }catch(NullPointerException e){
            e.printStackTrace();
        }
        
    }
}
