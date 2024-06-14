import { Create } from "react-admin";
import { ShipmentForm } from "../components/shipment-form";
import { fileToBase64 } from "../../common/util/misc-util";

export function ShipmentCreate() {
  return (
    <Create
      transform={async (data) => ({
        ...data,
        packingLists: data.packingLists.map((list) => ({ id: list })),
        customsDocuments: data.customsDocuments
          ? [
              {
                content: await fileToBase64(data.customsDocuments.rawFile),
                name: data.customsDocuments.title,
                fileType: "pdf",
              },
            ]
          : [],
      })}
    >
      <ShipmentForm />
    </Create>
  );
}
