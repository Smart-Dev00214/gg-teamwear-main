import { Admin, Resource } from "react-admin";
import {
  PackingListList,
  PackingListEdit,
  PackingListShow,
} from "./packing-list";
import { ShipmentCreate, ShipmentList, ShipmentShow } from "./shipment";
import { dataProvider } from "./data-provider";
import React from "react";

const App = () => (
  <React.Fragment>
    <Admin dataProvider={dataProvider}>
      <Resource
        name="packing-list"
        recordRepresentation="documentNumber"
        list={PackingListList}
        edit={PackingListEdit}
        // create={PackingListCreate}
        show={PackingListShow}
      />
      <Resource
        name="shipment"
        create={ShipmentCreate}
        list={ShipmentList}
        show={ShipmentShow}
      />
      <Resource name="shipment-package" />
    </Admin>
    <div
      style={{
        position: "static",
        right: 0,
        bottom: 0,
        left: 0,
        zIndex: 100,
        padding: 6,
        textAlign: "center",
        color: "#FFFFFF",
        backgroundColor: "#2196f3",
        boxShadow:
          "0px -2px 4px -1px rgba(0,0,0,0.2),0px -4px 5px 0px rgba(0,0,0,0.14),0px -1px 10px 0px rgba(0,0,0,0.12)",
        fontFamily: '"Roboto","Helvetica","Arial",sans-serif',
      }}
    >
      © 2023 Sadaor Srl
    </div>
  </React.Fragment>
);

export default App;
