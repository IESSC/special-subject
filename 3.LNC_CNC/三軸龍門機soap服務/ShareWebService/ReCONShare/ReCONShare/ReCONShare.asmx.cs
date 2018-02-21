using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;
using ReCONShare.ServiceReference1;
using Newtonsoft.Json;

namespace ReCONShare
{
    /// <summary>
    ///ReCONShare 的摘要描述
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // 若要允許使用 ASP.NET AJAX 從指令碼呼叫此 Web 服務，請取消註解下列一行。
    // [System.Web.Script.Services.ScriptService]
    public class ReCONShare : System.Web.Services.WebService
    {

        [WebMethod]
        public string GetPollingData()
        {
            ReconWcfServiceClient ServiceConnection = new ReconWcfServiceClient();
            ServiceConnection.Open();
            Class_ReCONSync_Service[] Data = ServiceConnection.GetPollingData();
            ServiceConnection.Close();
            PollingDataRoot RootObj = new PollingDataRoot();
            RootObj.Data = Data;
            return JsonConvert.SerializeObject(RootObj);
        }

        [WebMethod]
        public bool ReconServiceStatus()
        {
            ReconWcfServiceClient ServiceConnection = new ReconWcfServiceClient();
            ServiceConnection.Open();
            bool Status = ServiceConnection.ReconServiceStatus();
            ServiceConnection.Close();
            return Status;
        }

        [WebMethod]
        public bool WriteRBit(string ServerIndex, string R_Value_address, string ElecValue, string Trigger)
        {
            ReconWcfServiceClient ServiceConnection = new ReconWcfServiceClient();
            ServiceConnection.Open();
            bool Flag = ServiceConnection.Write_R_Bit(ServerIndex, R_Value_address, ElecValue, Trigger);
            ServiceConnection.Close();
            return Flag;
        }
    }
}
